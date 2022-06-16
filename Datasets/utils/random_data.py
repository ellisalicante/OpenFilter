import os
import random
import shutil
import pdb


def absoluteFilePaths(directory):
    abspaths = []
    for dirr, fols, _ in os.walk(directory):
        for fol in fols:
            dirfol = os.path.join(dirr, fol)
            for dirpath, folders, _ in os.walk(dirfol):
                for folder in folders:
                    for _, _, files in os.walk(os.path.join(dirpath, folder)):
                        for file in files:
                            abspaths.append(os.path.join(dirpath, folder, file))

    return abspaths

if __name__ == '__main__':
    directory = '/mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter_final'
    #directory = '/mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_one_filter'
    abspaths = absoluteFilePaths(directory)

    # Copy all to a common folder for sanity check
    dest = '/mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_all_final'
    for i, path in enumerate(abspaths):
        if os.path.exists(os.path.join(dest, path.split('/')[-1])):
            new_filename = path.split('/')[-1].split('.')[0] + '_{}'.format(int(i/12000)) + '.png'
            print('Copying {} -> {}'.format(path, os.path.join(dest, new_filename)))
            shutil.copy(path, os.path.join(dest, new_filename))
        else:
            print('Copying {} -> {}'.format(path, os.path.join(dest, path.split('/')[-1])))
            shutil.copy(path, os.path.join(dest, path.split('/')[-1]))
    
    # Copy to final B-LFW dataset
    '''
    random_filter_set = []
    for i in range(12000):
        filter = random.randint(0, 7)
        random_filter_set.append(abspaths[filter*12000 + i])

    dest = '/mnt/c/Users/Bill/Desktop/lfw_align_112_png_beauty_random_final'
    for path in random_filter_set:
        print('Copying {} -> {}'.format(path, os.path.join(dest, path.split('/')[-1])))
        shutil.copy(path, os.path.join(dest, path.split('/')[-1]))
    '''