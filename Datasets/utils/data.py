import numpy as np
import bcolz
import os
import pdb
from PIL import Image
import torch
import cv2

def get_pair(root, name):
    carray = bcolz.carray(rootdir = os.path.join(root, name), mode='r')
    issame = np.load('{}/{}_list.npy'.format(root, name))
    return carray, issame

def get_data(data_root):
    #agedb_30, agedb_30_issame = get_pair(data_root, 'agedb_30')
    #cfp_fp, cfp_fp_issame = get_pair(data_root, 'cfp_fp')
    lfw, lfw_issame = get_pair(data_root, 'lfw')
    #vgg2_fp, vgg2_fp_issame = get_pair(data_root, 'vgg2_fp')
    return lfw, lfw_issame#agedb_30, cfp_fp, lfw, vgg2_fp, agedb_30_issame, cfp_fp_issame, lfw_issame, vgg2_fp_issame


#lfw, lfw_issame = get_data("/home/bill/datasets/lfw/lfw_align_112")

# Load issame list
#issame = np.load('/home/bill/datasets/lfw/issame.npy')
#issame = issame.tolist()

# Create original and flipped face images tensors
original = np.zeros((12000, 3, 112, 112))
flipped = np.zeros((12000, 3, 112, 112))

cnt = 0

# Define dataset path and sort it
dataset_path = '/mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_random_final'

if 'random' not in dataset_path:
    # Use this if naming is: sets first, filters second 
    folders = sorted(os.listdir(dataset_path))
    folders = sorted(folders, key = lambda x: x[4])

    # Original images -> np.array()
    for folder in folders:
        folder_path = os.path.join(dataset_path, folder)
        folder_images = sorted(os.listdir(folder_path))
        for folder_image in folder_images:
            print('Reading image: {}'.format(folder_image))
            img = np.array(Image.open(os.path.join(folder_path, folder_image)))
            img = img.transpose(2,0,1)
            img = np.float32(img)
            img = torch.from_numpy(img)
            original[cnt, :, :, :] = img
            cnt += 1
            
            # cv2.imwrite('test_orig.png', img.detach().numpy().transpose(1,2,0))
else:
    for folder_image in [x for x in os.listdir(dataset_path) if x.endswith('png')]:
        print('Reading image: {}'.format(folder_image))
        img = np.array(Image.open(os.path.join(dataset_path, folder_image)))
        img = img.transpose(2,0,1)
        img = np.float32(img)
        img = torch.from_numpy(img)
        original[cnt, :, :, :] = img
        cnt += 1
        
        # cv2.imwrite('test_orig.png', img.detach().numpy().transpose(1,2,0)) 

# Save into .npy file and then delete from memory
np.save(os.path.join(dataset_path, 'lfw_original.npy'), original)
del original 

cnt = 0

if 'random' not in dataset_path:
    # Flipped images -> np.array()
    for folder in folders:
        folder_path = os.path.join(dataset_path, folder)
        folder_images = sorted(os.listdir(folder_path))
        for folder_image in folder_images:
            print('Reading image: {}'.format(folder_image))
            img = np.array(Image.open(os.path.join(folder_path, folder_image)))
            img = img.transpose(2,0,1)
            img = np.float32(img)
            img = torch.from_numpy(img)
            flip = torch.flip(img, [2])
            flipped[cnt, :, :, :] = flip
            cnt += 1

            # cv2.imwrite('test_flip_2.png', flip.detach().numpy().transpose(1,2,0))
else:
    for folder_image in [x for x in os.listdir(dataset_path) if x.endswith('png')]:
        print('Reading image: {}'.format(folder_image))
        img = np.array(Image.open(os.path.join(dataset_path, folder_image)))
        img = img.transpose(2,0,1)
        img = np.float32(img)
        img = torch.from_numpy(img)
        flip = torch.flip(img, [2])
        flipped[cnt, :, :, :] = flip
        cnt += 1
    
        # cv2.imwrite('test_orig.png', img.detach().numpy().transpose(1,2,0)) 


# Save into .npy file and then delete from memory
np.save(os.path.join(dataset_path, 'lfw_flipped.npy'), flipped)
del flipped 