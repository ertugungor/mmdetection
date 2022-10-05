_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection_train_subset_oversampling.py',
    '../_base_/schedules/schedule_2x.py', '../_base_/default_runtime.py'
]
# _base_ = [
#     '../_base_/models/faster_rcnn_r50_fpn.py',
#     '../_base_/datasets/coco_detection_train_subset.py',
#     '../_base_/schedules/schedule_2x.py', '../_base_/default_runtime.py'
# ]
