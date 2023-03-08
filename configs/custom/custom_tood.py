# the new config inherits the base configs to highlight the necessary modification
_base_ = '../tood/tood_r101_fpn_dconv_c3-c5_mstrain_2x_coco.py'

# 1. dataset settings
dataset_type = 'CocoDataset'
classes = ('vehicle', 'person')
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='train.json',
        img_prefix='train'),
    val=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='val.json',
        img_prefix='val'),
    test=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='val.json',
        img_prefix='val'))

model = dict(
    type='TOOD',
    bbox_head=dict(
        type='TOODHead',
        num_classes=2))

load_from = 'checkpoints/tood_r101_fpn_dconv_c3-c5_mstrain_2x_coco_20211210_213728-4a824142.pth'
