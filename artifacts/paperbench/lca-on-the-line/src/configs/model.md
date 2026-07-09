# Model Configuration

## Vision Models (VMs) — 36 total
- **Source**: torchvision (pretrained on ImageNet with cross-entropy loss on class labels)
- **Models**:
  - AlexNet: alexnet
  - ConvNeXt: convnext_tiny
  - DenseNet: densenet121, densenet161, densenet169, densenet201
  - EfficientNet: efficientnet_b0
  - GoogLeNet: googlenet
  - InceptionV3: inceptionV3
  - MnasNet: mnasnet0.5, mnasnet0.75, mnasnet1.0, mnasnet1.3
  - MobileNetV3: mobilenetv3_small, mobilenetv3_large
  - RegNet: regnet_y_1_6gf
  - Wide ResNet: wide_resnet101_2
  - ResNet: resnet18, resnet34, resnet50, resnet101, resnet152
  - ShuffleNet: shufflenet_v2_x2_0
  - SqueezeNet: squeezenet1_0, squeezenet1_1
  - Swin Transformer: swin_b
  - VGG: vgg11, vgg13, vgg16, vgg19, vgg11_bn, vgg13_bn, vgg16_bn, vgg19_bn
  - ViT: vit_b_32, vit_l_32

## Vision-Language Models (VLMs) — 39 total
- **Source**: OpenCLIP (https://github.com/mlfoundations/open_clip) and CLIP (https://github.com/openai/CLIP)
- **Models**:
  - ALBEF: albef_feature_extractor
  - BLIP: blip_feature_extractor_base
  - CLIP (openai): RN50, RN101, RN50x4, ViT-B-32, ViT-B-16, ViT-L-14, ViT-L-14-336px
  - OpenCLIP: 
    - openCLIP_('RN101', 'openai')
    - openCLIP_('RN101', 'yfcc15m')
    - openCLIP_('RN101-quickgelu', 'openai')
    - openCLIP_('RN101-quickgelu', 'yfcc15m')
    - openCLIP_('RN50', 'cc12m')
    - openCLIP_('RN50', 'openai')
    - openCLIP_('RN50', 'yfcc15m')
    - openCLIP_('RN50-quickgelu', 'cc12m')
    - openCLIP_('RN50-quickgelu', 'openai')
    - openCLIP_('RN50-quickgelu', 'yfcc15m')
    - openCLIP_('RN50x16', 'openai')
    - openCLIP_('RN50x4', 'openai')
    - openCLIP_('RN50x64', 'openai')
    - openCLIP_('ViT-B-16', 'laion2b_s34b_b88k')
    - openCLIP_('ViT-B-16', 'laion400m_e31')
    - openCLIP_('ViT-B-16', 'laion400m_e32')
    - openCLIP_('ViT-B-16-plus-240', 'laion400m_e31')
    - openCLIP_('ViT-B-16-plus-240', 'laion400m_e32')
    - openCLIP_('ViT-B-32', 'laion2b_e16')
    - openCLIP_('ViT-B-32', 'laion2b_s34b_b79k')
    - openCLIP_('ViT-B-32', 'laion400m_e31')
    - openCLIP_('ViT-B-32', 'laion400m_e32')
    - openCLIP_('ViT-B-32', 'openai')
    - openCLIP_('ViT-B-32-quickgelu', 'laion400m_e31')
    - openCLIP_('ViT-B-32-quickgelu', 'laion400m_e32')
    - openCLIP_('ViT-L-14', 'laion2b_s32b_b82k')
    - openCLIP_('ViT-L-14', 'laion400m_e31')
    - openCLIP_('ViT-L-14', 'laion400m_e32')
    - openCLIP_('coca_ViT-B-32', 'laion2b_s13b_90k')
    - openCLIP_('coca_ViT-L-14', 'laion2b_s13b_90k')

## Linear Probe Architecture
- **Structure**: Frozen backbone → extract pre-classifier features → new linear layer → 1000-dim output → softmax
- **The linear layer maps**: last hidden layer dimension → 1000 (ImageNet classes)
- **Backbone frozen**: Yes (only linear head is trained)

## ImageNet Classification Setup (for Top-1/Top-5 eval)
- **Number of classes**: 1000
- **Preprocessing**: Standard ImageNet normalization (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
- **Resize**: Not specified in paper (standard per model)
