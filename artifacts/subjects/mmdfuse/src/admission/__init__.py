"""Released-code MMD-FUSE admission, with explicit target and intervention ancestry."""
from .protocol import (
    control_passes,
    frozen_control_configuration,
    make_row_manifest,
    map_request,
    require_released_attribution,
    validate_row_manifest,
    verify_baseline,
)

__all__ = ['control_passes', 'frozen_control_configuration', 'make_row_manifest', 'map_request',
           'require_released_attribution', 'validate_row_manifest', 'verify_baseline']
