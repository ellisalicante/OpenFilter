import os
import pdb
from random import gauss
import shutil
import numpy as np
import torch

from PIL import Image, ImageFilter
#from elasticface.backbones.iresnet import iresnet100

fairfaces_val = '/mnt/c/Users/Bill/Desktop/fairfaces_val'
fairbeauty_val = '/mnt/c/Users/Bill/Desktop/fairbeauty_val'
fairfaces_train = '/mnt/c/Users/Bill/Desktop/fairfaces_train/train_fair'

# Copy corresponding images from faifaces_train -> fairfaces_val
copy = False
if copy:
    for dirpath, folders, files in os.walk(fairbeauty_val):
        for folder in folders:
            for _, _, files in os.walk(os.path.join(dirpath, folder)):
                abspaths = []
                for file in files:
                    abspaths.append(os.path.join(dirpath, folder, file))
            
            assert len(abspaths) == 1000

            if not os.path.exists(os.path.join(fairfaces_val, folder)):
                os.makedirs(os.path.join(fairfaces_val, folder))
            
            for file in abspaths:
                print('Copying {} -> {}'.format(os.path.join(fairfaces_train, file.split('/')[-1]), os.path.join(fairfaces_val, folder, file.split('/')[-1])))
                shutil.copy(os.path.join(fairfaces_train, file.split('/')[-1]), os.path.join(fairfaces_val, folder, file.split('/')[-1]))


size = 112
# Convert images to numpy arrays for inference
# Change the path
convert=True

gaussian_2=False
gaussian_3=False
pixelation=False
if convert:
    for dirpath, folders, files in os.walk(fairbeauty_val):
        for folder in folders:
            for _, _, files in os.walk(os.path.join(dirpath, folder)):
                images = np.zeros((1000, 3, size, size))
                cnt = 0
                for file in [x for x in files if x.endswith('png')]:
                    print('Reading image: {}'.format(os.path.join(dirpath, folder, file)))
                    img = Image.open(os.path.join(dirpath, folder, file))
                    #print('Size: {}'.format(img.size))
                    img = img.resize((size, size), resample=Image.BILINEAR)
                    
                    #img.save(os.path.join(dirpath + '_112', folder, file))
                    
                    if gaussian_2:
                        img = img.filter(ImageFilter.GaussianBlur(2))
                        img.save(os.path.join(dirpath + '_gaussian_2', folder, file))
                    elif gaussian_3:
                        img = img.filter(ImageFilter.GaussianBlur(3))
                        img.save(os.path.join(dirpath + '_gaussian_3', folder, file))
                    elif pixelation:
                        img = img.resize((64, 64), resample=Image.BILINEAR).resize(img.size,Image.NEAREST)
                        img.save(os.path.join(dirpath + '_pixelation', folder, file))

                    img = np.array(img)
                    img = img.transpose(2,0,1)
                    img = np.float32(img)
                    img = torch.from_numpy(img)
                    images[cnt, :, :, :] = img
                    cnt += 1
                
                print('Saving numpy array into: {}'.format(os.path.join(dirpath, folder)))
                if gaussian_2:
                    np.save(os.path.join(os.path.join(dirpath, folder), 'images_gaussian_2.npy'), images)
                elif gaussian_3:
                    np.save(os.path.join(os.path.join(dirpath, folder), 'images_gaussian_3.npy'), images)
                elif pixelation:
                    np.save(os.path.join(os.path.join(dirpath, folder), 'images_pixelation.npy'), images)
                else:
                    np.save(os.path.join(os.path.join(dirpath, folder), 'images.npy'), images)
                

compute_dist = False
dists = dict()
dists['00'] = dict()
dists['01'] = dict()
dists['02'] = dict()

if compute_dist:
    for dirpath, folders, files in os.walk(fairfaces_val):
        for folder in folders:
            for _, _, files in os.walk(os.path.join(dirpath, folder)):
                dists[folder]['orig_dist'] = np.load(os.path.join(dirpath, folder, 'elasticface_dist.npy'))
                dists[folder]['gaussian_2_dist'] = np.load(os.path.join(dirpath, folder, 'elasticface_dist_gaussian_2.npy'))
                dists[folder]['gaussian_3_dist'] = np.load(os.path.join(dirpath, folder, 'elasticface_dist_gaussian_3.npy'))
                dists[folder]['pixelation_dist'] = np.load(os.path.join(dirpath, folder, 'elasticface_dist_pixelation.npy'))
    
    for dirpath, folders, files in os.walk(fairbeauty_val):
        for folder in folders:
            for _, _, files in os.walk(os.path.join(dirpath, folder)):
                dists[folder]['beauty_dist'] = np.load(os.path.join(dirpath, folder, 'elasticface_dist.npy'))

pdb.set_trace()











'''
# Elasticface inference
embed_size = 512
gpu_id = 0
output_folder='/home/bill/code/face_recognition/elasticface/models'
weights=os.listdir(output_folder)
for w in weights:
    if "backbone" in w:
        backbone = iresnet100(num_features=embed_size).to(f"cuda:{gpu_id}")
        backbone.load_state_dict(torch.load(os.path.join(output_folder,w)))
        model = torch.nn.DataParallel(backbone, device_ids=[gpu_id])
        
        #backbone.eval()
        #norm_dist = callback_verification(int(w.split("backbone")[0]), model)

        #np.save(os.path.join(cfg.rec, 'elasticface_dist.npy'), norm_dist)
'''





'''
    def __init__(self, frequent, rank, val_targets, rec_prefix, image_size=(112, 112)):
        self.frequent: int = frequent
        self.rank: int = rank
        self.highest_acc: float = 0.0
        self.highest_acc_list: List[float] = [0.0] * len(val_targets)
        self.ver_list: List[object] = []
        self.ver_name_list: List[str] = []
        if self.rank == 0:
            self.init_dataset(val_targets=val_targets, data_dir=rec_prefix, image_size=image_size)


    def __call__(self, num_update, backbone: torch.nn.Module):
        if self.rank == 0 and num_update > 0 and num_update % self.frequent == 0:
            backbone.eval()
            norm_dist = self.ver_test(backbone, num_update)
            backbone.train()
        
        return norm_dist


    def ver_test(self, backbone: torch.nn.Module, global_step: int):
        results = []
        for i in range(len(self.ver_list)):
            acc1, std1, acc2, std2, xnorm, embeddings_list, norm_dist = verification.test(
                self.ver_list[i], backbone, 10, 10)
            logging.info('[%s][%d]Sum of Euclidean dists: %f' % (self.ver_name_list[i], global_step, np.sum(norm_dist)))
            logging.info('[%s][%d]XNorm: %f' % (self.ver_name_list[i], global_step, xnorm))
            logging.info('[%s][%d]Accuracy-Flip: %1.5f+-%1.5f' % (self.ver_name_list[i], global_step, acc2, std2))
            if acc2 > self.highest_acc_list[i]:
                self.highest_acc_list[i] = acc2
            logging.info(
                '[%s][%d]Accuracy-Highest: %1.5f' % (self.ver_name_list[i], global_step, self.highest_acc_list[i]))
            results.append(acc2)

        return norm_dist

def test(data_set, backbone, batch_size, nfolds=10):
    print('testing verification..')
    data_list = data_set[0]
    issame_list = data_set[1]
    embeddings_list = []
    time_consumed = 0.0
    for i in range(len(data_list)):
        data = data_list[i]
        embeddings = None
        ba = 0
        while ba < data.shape[0]:
            bb = min(ba + batch_size, data.shape[0])
            count = bb - ba
            _data = data[bb - batch_size: bb]
            time0 = datetime.datetime.now()
            img = ((_data / 255) - 0.5) / 0.5
            net_out: torch.Tensor = backbone(img)
            _embeddings = net_out.detach().cpu().numpy()
            time_now = datetime.datetime.now()
            diff = time_now - time0
            time_consumed += diff.total_seconds()
            if embeddings is None:
                embeddings = np.zeros((data.shape[0], _embeddings.shape[1]))
            embeddings[ba:bb, :] = _embeddings[(batch_size - count):, :]
            ba = bb
        embeddings_list.append(embeddings)

    _xnorm = 0.0
    _xnorm_cnt = 0
    for embed in embeddings_list:
        for i in range(embed.shape[0]):
            _em = embed[i]
            _norm = np.linalg.norm(_em)
            _xnorm += _norm
            _xnorm_cnt += 1
    _xnorm /= _xnorm_cnt

    embeddings = embeddings_list[0].copy()
    embeddings = sklearn.preprocessing.normalize(embeddings)
    acc1 = 0.0
    std1 = 0.0
    embeddings = embeddings_list[0] + embeddings_list[1]
    embeddings = sklearn.preprocessing.normalize(embeddings)
    print(embeddings.shape)
    print('infer time', time_consumed)
    _, _, accuracy, val, val_std, far, norm_dist =  evaluate(embeddings, issame_list, nrof_folds=nfolds)
    acc2, std2 = np.mean(accuracy), np.std(accuracy)
    
    return acc1, std1, acc2, std2, _xnorm, embeddings_list, norm_dist
'''