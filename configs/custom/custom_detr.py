_base_ = '../detr/detr_r50_8x2_150e_coco.py'
classes = ('vehicle', 'person')
model = dict(
    type='DETR',
    bbox_head=dict(
        type='DETRHead',
        num_classes=2))

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

# We can use the pre-trained Faster RCNN model to obtain higher performance
load_from = 'checkpoints/detr_r50_8x2_150e_coco_20201130_194835-2c4b8974.pth'
