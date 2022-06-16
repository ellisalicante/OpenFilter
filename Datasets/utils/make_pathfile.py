import os
import numpy as np
import pdb
from posixpath import abspath

def absoluteFilePaths(directory):
    abspaths = []
    f = open(os.path.join(directory, "images.txt"), "w")
    if 'random' not in directory and 'fair' not in directory:
        for dirpath, folders, _ in os.walk(directory):
            for folder in folders:
                for _, _, files in os.walk(os.path.join(dirpath, folder)):
                    for file in files:
                        abspaths.append(os.path.join(dirpath, folder, file))
                        f.write(os.path.abspath(os.path.join(dirpath, folder, file)))
                        f.write('\n')
                        #print(os.path.abspath(os.path.join(dirpath, folder, file)))
    else:
        for dirpath, _, files in os.walk(directory):
            for file in [x for x in files if x.endswith('png')]:
                abspaths.append(os.path.join(dirpath, file))
                f.write(os.path.abspath(os.path.join(dirpath, file)))
                f.write('\n')


    f.close()
    return abspaths

if __name__ == '__main__':
    #directory = '/mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_random_final'
    directory = '/mnt/c/Users/Bill/Desktop/fairfaces_val_112/02'
    abspaths = absoluteFilePaths(directory)

    '''
    directory = '/mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter'
    issame = np.load(os.path.join(directory, 'issame.npy')
    issame = issame.tolist()
    f = open(os.path.join(directory, "issame.txt"), "w")
    f.write(issame)
    f.close()
    '''