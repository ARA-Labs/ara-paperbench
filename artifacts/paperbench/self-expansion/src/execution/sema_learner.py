"""
SEMA Learner: Training loop, outlier detection, and optimizer management.
Implements the continual learning training protocol for SEMA.

Source: models/sema.py
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import numpy as np

from src.execution.sema_core import SEMAModules


def get_trainable_params(network, phase: str):
    """
    Returns trainable parameters for a given training phase.

    Args:
        network: SEMAVitNet model
        phase: 'func' (functional adapters + router + head) or 'rd' (representation descriptors)
    Returns:
        List of parameters with requires_grad=True for the given phase
    """
    if phase == 'func':
        return [p for n, p in network.named_parameters()
                if ('functional' in n or 'router' in n or 'fc' in n) and p.requires_grad]
    elif phase == 'rd':
        return [p for n, p in network.named_parameters()
                if 'rd' in n and p.requires_grad]
    raise ValueError(f"Unknown phase: {phase}")


def make_optimizer_and_scheduler(params, optimizer_type: str = 'sgd',
                                 lr: float = 0.005, momentum: float = 0.9,
                                 weight_decay: float = 0.0005,
                                 num_epoch: int = 20, min_lr: float = 0.0):
    """
    Build SGD/AdamW optimizer + CosineAnnealingLR scheduler.

    Args:
        params: Iterable of parameters to optimize
        optimizer_type: 'sgd' or 'adam'
        lr: Initial learning rate
        momentum: SGD momentum (ignored for adam)
        weight_decay: L2 regularization
        num_epoch: T_max for CosineAnnealingLR
        min_lr: eta_min for CosineAnnealingLR
    """
    if optimizer_type == 'sgd':
        optimizer = optim.SGD(params, momentum=momentum, lr=lr, weight_decay=weight_decay)
    elif optimizer_type == 'adam':
        optimizer = optim.AdamW(params, lr=lr, weight_decay=weight_decay)
    else:
        raise ValueError(f"Unknown optimizer: {optimizer_type}")
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=num_epoch, eta_min=min_lr)
    return optimizer, scheduler


def train_one_phase(network, train_loader: DataLoader, optimizer, scheduler,
                    num_epoch: int, phase: str, total_classes: int,
                    known_classes: int, cur_task: int, device: str = 'cuda'):
    """
    Train network for num_epoch epochs in a given phase.

    Args:
        network: SEMAVitNet
        train_loader: DataLoader for current task
        optimizer: Optimizer for current phase
        scheduler: LR scheduler
        num_epoch: Number of epochs
        phase: 'func' (CE loss) or 'rd' (reconstruction loss)
        total_classes: Total seen classes so far
        known_classes: Classes seen before current task
        cur_task: Current task index
        device: 'cuda' or 'cpu'
    """
    network.train()
    for epoch in range(num_epoch):
        for _, inputs, targets in train_loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outcome = network(inputs)

            if phase == 'func':
                logits = outcome['logits'][:, :total_classes]
                if cur_task > 0:
                    logits[:, :known_classes] = -float('inf')
                loss = nn.functional.cross_entropy(logits, targets)
            elif phase == 'rd':
                loss = outcome['rd_loss']

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        scheduler.step()


def detect_and_expand(network, detect_loader: DataLoader, train_loader: DataLoader,
                      args: dict, total_classes: int, known_classes: int,
                      cur_task: int, device: str = 'cuda') -> int:
    """
    Scan detection loader; trigger expansion and training if z-score fires.
    Recursive: re-scans after expansion to check for more expansions (deeper layers).

    Returns:
        Number of layers expanded in this call chain.
    """
    is_added = False
    for _, inputs, targets in detect_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        outcome = network(inputs)
        added_record = outcome.get('added_record', [])

        if any(added_record):
            is_added = True
            # Disable outlier detection during training
            _set_detecting_outlier(network, False)

            # Train the newly added adapter
            func_params = get_trainable_params(network, 'func')
            func_opt, func_sched = make_optimizer_and_scheduler(
                func_params, optimizer_type=args['optimizer'], lr=args['init_lr'],
                weight_decay=args['weight_decay'], num_epoch=args['func_epoch'], min_lr=args.get('min_lr', 0)
            )
            train_one_phase(network, train_loader, func_opt, func_sched,
                            args['func_epoch'], 'func', total_classes, known_classes, cur_task, device)

            rd_params = get_trainable_params(network, 'rd')
            rd_opt, rd_sched = make_optimizer_and_scheduler(
                rd_params, optimizer_type=args['optimizer'], lr=args['rd_lr'],
                weight_decay=args['weight_decay'], num_epoch=args['rd_epoch'], min_lr=args.get('min_lr', 0)
            )
            train_one_phase(network, train_loader, rd_opt, rd_sched,
                            args['rd_epoch'], 'rd', total_classes, known_classes, cur_task, device)

            # Freeze newly trained adapters and re-enable detection
            _freeze_newly_added(network)
            _set_detecting_outlier(network, True)

    if is_added:
        # Recurse: check deeper layers for expansion
        return 1 + detect_and_expand(network, detect_loader, train_loader, args,
                                     total_classes, known_classes, cur_task, device)
    return 0


def _set_detecting_outlier(network, value: bool):
    """Toggle detecting_outlier flag on all SEMAModules."""
    for module in network.modules():
        if isinstance(module, SEMAModules):
            module.detecting_outlier = value


def _freeze_newly_added(network):
    """Freeze functional adapters, RDs, and reset newly_added status."""
    for module in network.modules():
        if isinstance(module, SEMAModules):
            module._freeze_all_functional()
            module._freeze_all_rds()
            module._reset_newly_added()


def sema_incremental_train(network, data_manager, args: dict, cur_task: int,
                           known_classes: int, total_classes: int, device: str = 'cuda'):
    """
    Full SEMA training protocol for one task.

    For task 0: train func adapters (phase='func') + RDs (phase='rd').
    For task t>0: scan for expansion; if no expansion, still train func adapters
                  (to update router with existing frozen adapters).
    After training: freeze all, end_of_task_training().

    Args:
        network: SEMAVitNet
        data_manager: DataManager providing train/test datasets
        args: Config dict from JSON
        cur_task: Current task index (0-indexed)
        known_classes: Number of classes seen before this task
        total_classes: Total classes after this task
        device: Compute device
    """
    train_loader = DataLoader(
        data_manager.get_dataset(range(known_classes, total_classes), 'train', 'train'),
        batch_size=args['batch_size'], shuffle=True, num_workers=8
    )

    if cur_task == 0:
        # First task: train everything from scratch
        func_params = get_trainable_params(network, 'func')
        func_opt, func_sched = make_optimizer_and_scheduler(
            func_params, args['optimizer'], args['init_lr'],
            weight_decay=args['weight_decay'], num_epoch=args['func_epoch'], min_lr=args.get('min_lr', 0)
        )
        train_one_phase(network, train_loader, func_opt, func_sched,
                        args['func_epoch'], 'func', total_classes, known_classes, cur_task, device)

        rd_params = get_trainable_params(network, 'rd')
        rd_opt, rd_sched = make_optimizer_and_scheduler(
            rd_params, args['optimizer'], args['rd_lr'],
            weight_decay=args['weight_decay'], num_epoch=args['rd_epoch'], min_lr=args.get('min_lr', 0)
        )
        train_one_phase(network, train_loader, rd_opt, rd_sched,
                        args['rd_epoch'], 'rd', total_classes, known_classes, cur_task, device)
    else:
        _set_detecting_outlier(network, True)
        detect_loader = DataLoader(
            data_manager.get_dataset(range(known_classes, total_classes), 'train', 'train'),
            batch_size=args['detect_batch_size'], shuffle=True, num_workers=8
        )
        added = detect_and_expand(network, detect_loader, train_loader, args,
                                  total_classes, known_classes, cur_task, device)
        _set_detecting_outlier(network, False)

        if added == 0:
            # No expansion: train existing adapters (router update only — new router columns frozen)
            func_params = get_trainable_params(network, 'func')
            func_opt, func_sched = make_optimizer_and_scheduler(
                func_params, args['optimizer'], args['init_lr'],
                weight_decay=args['weight_decay'], num_epoch=args['func_epoch'], min_lr=args.get('min_lr', 0)
            )
            train_one_phase(network, train_loader, func_opt, func_sched,
                            args['func_epoch'], 'func', total_classes, known_classes, cur_task, device)

    # End of task: freeze all, merge router
    for module in network.modules():
        if isinstance(module, SEMAModules):
            module.end_of_task_training()
