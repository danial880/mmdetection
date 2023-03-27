_base_ = '../faster_rcnn/faster_rcnn_x101_64x4d_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=2)))

# Modify dataset related settings

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

train_pipeline = [
    dict(type='Resize', img_scale=(1888, 1300), keep_ratio=True)
]
test_pipeline = [
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1888, 1300),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
])
]
# We can use the pre-trained Faster RCNN model to obtain higher performance
#load_from = 'checkpoints/faster_rcnn_x101_64x4d_fpn_1x_coco_20200204-833ee192.pth'
