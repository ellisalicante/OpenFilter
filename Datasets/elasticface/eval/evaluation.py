import logging
import os

#import cv2
import numpy as np
import sys
import torch
sys.path.append('/home/bill/code/face_recognition/elasticface')

from utils.utils_callbacks import CallBackVerification
from utils.utils_logging import init_logging

from config.config import config as cfg

from backbones.iresnet import iresnet100, iresnet50

if __name__ == "__main__":
    gpu_id = 0
    log_root = logging.getLogger()
    init_logging(log_root, 0, cfg.output,logfile="test1.log")
    logging.info('Running on: %s' % (cfg.rec.split('/')[-1]))
    callback_verification = CallBackVerification(1, 0, cfg.val_targets, cfg.rec)
    output_folder=cfg.output
    weights=os.listdir(output_folder)
    for w in weights:
        if "backbone" in w:
            if cfg.network == "iresnet100":
                backbone = iresnet100(num_features=cfg.embedding_size).to(f"cuda:{gpu_id}")
            elif cfg.network == "iresnet50":
                backbone = iresnet50(num_classes=cfg.embedding_size).to(f"cuda:{gpu_id}")
            else:
                backbone = None
                exit()
            backbone.load_state_dict(torch.load(os.path.join(output_folder,w)))
            model = torch.nn.DataParallel(backbone, device_ids=[gpu_id])
            norm_dist = callback_verification(int(w.split("backbone")[0]),model)

            #np.save(os.path.join(cfg.rec, 'elasticface_dist.npy'), norm_dist)

