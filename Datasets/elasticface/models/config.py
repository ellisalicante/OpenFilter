from easydict import EasyDict as edict

config = edict()
config.dataset = "emore"
config.embedding_size = 512
config.sample_rate = 1.0
config.fp16 = False
config.momentum = 0.9
config.weight_decay = 5e-4
config.weight_decay_last = 5e-3

config.batch_size = 128
config.lr = 0.1  # batch size is 512
config.output = "output_neurosip/emore_RandomCosFace_resnet_std0.05"
config.global_step=295672
config.s=64.0  # for fine tunning with cos 0.32 and m 0.45 # train cos from scratch 64 and 0.4
config.m=0.35

#net paramerters
config.net_name="resnet"
if (config.net_name=="mobilefacenet"):
    config.embedding_size = 128
config.net_size="s"
config.scale=1.0
config.gdw_size=1024 #512



if config.dataset == "emore":
    config.rec = "/data/fboutros/faces_emore"
    config.num_classes = 85742
    config.num_image = 5822653
    config.num_epoch =  26
    config.warmup_epoch = -1
    config.val_targets = ["lfw", "cfp_fp", "agedb_30" ,"calfw"]
    config.eval_step=5686

    def lr_step_func(epoch):
        return ((epoch + 1) / (4 + 1)) ** 2 if epoch < -1 else 0.1 ** len(
            [m for m in [8, 14,20,25] if m - 1 <= epoch])  # [m for m in [8, 14,20,25] if m - 1 <= epoch])
    config.lr_func = lr_step_func
if config.dataset == "emore2":
    config.rec = "/data/fboutros/faces_emore"
    config.num_classes = 81801
    config.num_image = 4075855
    config.num_epoch =  26
    config.warmup_epoch = -1
    config.val_targets = ["lfw", "cfp_fp", "agedb_30" ,"calfw"]
    config.eval_step=3980

    def lr_step_func(epoch):
        return ((epoch + 1) / (4 + 1)) ** 2 if epoch < -1 else 0.1 ** len(
            [m for m in [8, 14,20,25] if m - 1 <= epoch])  # [m for m in [8, 14,20,25] if m - 1 <= epoch])
    config.lr_func = lr_step_func
if config.dataset == "emore_stage2":
    config.m = 0.55
    config.lr = 0.00001  # batch size is 512
    config.rec = "/data/fboutros/faces_emore"
    config.num_classes = 85742
    config.num_image = 5822653
    config.num_epoch =  3
    config.warmup_epoch = -1
    config.val_targets = ["lfw", "cfp_fp", "agedb_30" ]
    def lr_step_func(epoch):
        return ((epoch + 1) / (4 + 1)) ** 2 if epoch < -1 else 0.1 ** len(
            [m for m in [ 3] if m - 1 <= epoch])  # [m for m in [8, 14,20,25] if m - 1 <= epoch])
    config.lr_func = lr_step_func
elif config.dataset == "emore_tune":
    config.rec = "/data/fboutros/faces_emore"
    config.num_classes = 85742
    config.num_image = 5822653
    config.num_epoch = 11
    config.warmup_epoch = -1
    config.val_targets = ["lfw", "cfp_fp", "agedb_30" ]

    def lr_step_func(epoch):
        return ((epoch + 1) / (4 + 1)) ** 2 if epoch < -1 else 0.1 ** len(
            [m for m in [4, 7] if m - 1 <= epoch])
    config.lr_func = lr_step_func
elif config.dataset == "ms1m-retinaface-t2":
    config.rec = "/train_tmp/ms1m-retinaface-t2"
    config.num_classes = 91180
    config.num_epoch = 25
    config.warmup_epoch = -1
    config.val_targets = ["lfw", "cfp_fp", "agedb_30"]

    def lr_step_func(epoch):
        return ((epoch + 1) / (4 + 1)) ** 2 if epoch < -1 else 0.1 ** len(
            [m for m in [11, 17, 22] if m - 1 <= epoch])
    config.lr_func = lr_step_func

elif config.dataset == "glint360k":
    config.rec = "/data/fboutros/glink/glint360k"
    config.num_classes = 360232
    config.num_image = 17091657
    config.num_epoch = 20
    config.warmup_epoch = -1
    config.val_targets = ["lfw", "cfp_fp", "agedb_30"]
    config.eval_step= 2000 #33350
    def lr_step_func(epoch):
        return ((epoch + 1) / (4 + 1)) ** 2 if epoch < config.warmup_epoch else 0.1 ** len(
            [m for m in [8, 12, 15, 18] if m - 1 <= epoch])
    config.lr_func = lr_step_func

elif config.dataset == "webface":
    config.rec = "/data/fboutros/faces_webface_112x112"
    config.global_step=18202
    config.num_classes = 10572
    config.num_image = 490623
    config.num_epoch = 50#34
    config.eval_step= 958 #33350
    config.lr = 0.1 #[20, 28, 32]  [28,38,46]

    config.warmup_epoch = -1
    config.val_targets = ["lfw", "cfp_fp", "agedb_30"]

    def lr_step_func(epoch):
        return ((epoch + 1) / (4 + 1)) ** 2 if epoch < config.warmup_epoch else 0.1 ** len(
            [m for m in [28, 38, 46] if m - 1 <= epoch])
    config.lr_func = lr_step_func

