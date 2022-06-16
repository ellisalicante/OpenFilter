import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets

import torch.nn.functional as F
from config import configurations
from backbone.model_resnet import ResNet_50, ResNet_101, ResNet_152
from backbone.model_irse import IR_50, IR_101, IR_152, IR_SE_50, IR_SE_101, IR_SE_152
from backbone.model_mobilefacenet import MobileFaceNet
from head.metrics import ArcFace, CurricularFace
from loss.focal import FocalLoss
from util.utils import get_val_data, get_val_pair, perform_val, get_time, AverageMeter, accuracy
from util.utils_logging import init_logging

from tqdm import tqdm
import os
import time
import numpy as np
import scipy
import pickle
import logging

if __name__ == '__main__':

    #======= hyperparameters & data loaders =======#
    cfg = configurations[1]
    torch.backends.cudnn.benchmark = True
    SEED = cfg['SEED'] # random seed for reproduce results
    torch.manual_seed(SEED)

    DATA_ROOT = cfg['DATA_ROOT'] # the parent root where your train/val/test data are stored
    BACKBONE_RESUME_ROOT = cfg['BACKBONE_RESUME_ROOT'] # the root to resume training from a saved checkpoint
    HEAD_RESUME_ROOT = cfg['HEAD_RESUME_ROOT']  # the root to resume training from a saved checkpoint

    BACKBONE_NAME = cfg['BACKBONE_NAME'] # support: ['ResNet_50', 'ResNet_101', 'ResNet_152', 'IR_50', 'IR_101', 'IR_152', 'IR_SE_50', 'IR_SE_101', 'IR_SE_152']
    HEAD_NAME = cfg['HEAD_NAME'] # support:  ['Softmax', 'ArcFace', 'CosFace', 'SphereFace', 'Am_softmax']
    INPUT_SIZE = cfg['INPUT_SIZE']
    BATCH_SIZE = cfg['BATCH_SIZE']
    RGB_MEAN = cfg['RGB_MEAN'] # for normalize inputs
    RGB_STD = cfg['RGB_STD']
    EMBEDDING_SIZE = cfg['EMBEDDING_SIZE'] # feature dimension
    GPU_ID = cfg['TEST_GPU_ID'] # specify your GPU ids
    #print("Overall Configurations:")
    #print(cfg)

    log_root = logging.getLogger()
    init_logging(log_root, 0, os.getcwd(), logfile="test_one_filter.log")
    logging.info('Running on: %s' % (DATA_ROOT.split('/')[-1]))
    data_dir = DATA_ROOT
    name = 'lfw'

    if 'beauty' in data_dir.split('/')[-1]:
        path = os.path.join(data_dir, name)
        imgs = []

        print('Reading original images...')
        original = np.load(path + '_original.npy')
        original = np.float32(original)
        original = original/255
        #import pdb;pdb.set_trace()
        #original = torch.from_numpy(original)

        imgs.append(original)
        del original

        print('Reading flipped images...')
        flipped = np.load(path + '_flipped.npy')
        flipped = np.float32(flipped)
        flipped = flipped/255
        #flipped = torch.from_numpy(flipped)
        
        imgs.append(flipped)
        del flipped

        print('Reading issame list...')
        issame = np.load(os.path.join('/'.join([str(elem) for elem in data_dir.split('/')[:-1]]), 'issame.npy'))
        #issame = issame.tolist()

        data_set = (imgs, issame)
        #import pdb;pdb.set_trace()
        # data_dir = '/mnt/c/Users/Bill/Desktop/lfw_align_112'
    elif '0' in data_dir.split('/')[-1]:
        imgs = []
        images = np.load(os.path.join(data_dir, 'images.npy'))
        images = np.float32(images)
        images = images/255
        #images = torch.from_numpy(images)
        imgs.append(images)
        imgs.append(images)
        
        issame = np.zeros((1000))
        issame = issame.tolist()

        data_set = (imgs, issame)
    else:
        lfw, lfw_issame = get_val_pair(data_dir, 'lfw')
        data_set = (lfw, lfw_issame)

        from PIL import Image
        im = Image.fromarray(lfw[0].T)
        im.save("lfw_0")

        im = Image.fromarray(data_set[0][0][0].T)
        im.save('dataset_0')
        
        #cfp_fp, cfp_fp_issame = get_val_pair(data_dir, 'cfp_fp')
        #agedb_30, agedb_30_issame = get_val_pair(data_dir, 'agedb_30')
        #calfw, calfw_issame = get_val_pair(data_dir, 'calfw')
        #cplfw, cplfw_issame = get_val_pair(data_dir, 'cplfw')

    #======= model =======#
    BACKBONE_DICT = {'ResNet_50': ResNet_50, 
                     'ResNet_101': ResNet_101, 
                     'ResNet_152': ResNet_152,
                     'IR_50': IR_50, 
                     'IR_101': IR_101, 
                     'IR_152': IR_152,
                     'IR_SE_50': IR_SE_50, 
                     'IR_SE_101': IR_SE_101, 
                     'IR_SE_152': IR_SE_152,
                     'MobileFaceNet': MobileFaceNet}

    BACKBONE = BACKBONE_DICT[BACKBONE_NAME](INPUT_SIZE)
    print("=" * 60)
    print("{} Backbone Generated".format(BACKBONE_NAME))
    print("=" * 60)
    if BACKBONE_RESUME_ROOT:
        print("=" * 60)
        if os.path.isfile(BACKBONE_RESUME_ROOT):
            print("Loading Backbone Checkpoint '{}'".format(BACKBONE_RESUME_ROOT))
            BACKBONE.load_state_dict(torch.load(BACKBONE_RESUME_ROOT))
        else:
            print("No Checkpoint Found at '{}'".format(BACKBONE_RESUME_ROOT))
            exit()
        print("=" * 60)

    BACKBONE.cuda()

    if len(GPU_ID) > 1:
        # multi-GPU setting
        BACKBONE = nn.DataParallel(BACKBONE, device_ids = GPU_ID)

    if 'beauty' in data_dir.split('/')[-1] or '0' in data_dir.split('/')[-1]:    
        accuracy_lfw, best_threshold_lfw, roc_curve_lfw, norm_dist = perform_val(EMBEDDING_SIZE, BATCH_SIZE, BACKBONE, data_set[0][0], data_set[1])
        logging.info("Evaluation: {} Acc: {}, Sum of Eucl Dists: {}, Best Threshold: {}".format(name, accuracy_lfw, np.sum(norm_dist), best_threshold_lfw))
        #print("Evaluation: {} Acc: {}, Sum of Eucl Dists: {}, Best Threshold: {}, ROC Curve {}".format(name, accuracy_lfw, name, best_threshold_lfw, name, roc_curve_lfw, norm_dist))
    else:
        accuracy_lfw, best_threshold_lfw, roc_curve_lfw, norm_dist = perform_val(EMBEDDING_SIZE, BATCH_SIZE, BACKBONE, data_set[0], data_set[1])
        logging.info("Evaluation: {} Acc: {}, Sum of Eucl Dists: {}, Best Threshold: {}".format(name, accuracy_lfw, np.sum(norm_dist), best_threshold_lfw))
        #print("Evaluation: {} Acc: {}, Sum of Eucl Dists: {}, Best Threshold: {}, ROC Curve {}".format(name, accuracy_lfw, name, best_threshold_lfw, name, roc_curve_lfw, norm_dist))

    np.save(os.path.join(DATA_ROOT, 'curricularface_dist.npy'), norm_dist)
    #accuracy_cfp_fp, best_threshold_cfp_fp, roc_curve_cfp_fp = perform_val(EMBEDDING_SIZE, BATCH_SIZE, BACKBONE, cfp_fp, cfp_fp_issame)
    #accuracy_agedb, best_threshold_agedb, roc_curve_agedb = perform_val(EMBEDDING_SIZE, BATCH_SIZE, BACKBONE, agedb, agedb_issame)
    #accuracy_calfw, best_threshold_calfw, roc_curve_calfw = perform_val(EMBEDDING_SIZE, BATCH_SIZE, BACKBONE, calfw, calfw_issame)
    #accuracy_cplfw, best_threshold_cplfw, roc_curve_cplfw = perform_val(EMBEDDING_SIZE, BATCH_SIZE, BACKBONE, cplfw, cplfw_issame)
    #print("Evaluation: LFW Acc: {}, CFP_FP Acc: {}, AgeDB Acc: {}, CPLFW Acc: {} CALFW Acc: {}".format(accuracy_lfw, accuracy_cfp_fp, accuracy_agedb, accuracy_cplfw, accuracy_calfw))
