_base_ = '../fcos/fcos_x101_64x4d_fpn_gn-head_mstrain_640-800_2x_coco.py'

model = dict(
            type='FCOS',
            bbox_head=dict(
                type='FCOSHead',
                num_classes=2))

classes = ('vehicle', 'person')
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='train.json',
        img_prefix='train'),
    val=dict(
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='val.json',
        img_prefix='val'),
    test=dict(
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='val.json',
        img_prefix='val'))

load_from = 'checkpoints/faster_rcnn_x101_64x4d_fpn_1x_coco_20200204-833ee192.pth'
