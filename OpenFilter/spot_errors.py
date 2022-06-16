import random
import time
import numpy as np
import os
import shutil
from PIL import Image
import argparse
    
def main(output, accepted_tuples=False):    
    if accepted_tuples:
        with open("accepted_tuples.txt", "r") as file:
            accepted_tuples = file.readlines()
        accepted_tuples = [(os.path.split(t.split()[0])[1], os.path.split(t.split()[1])[1]) for t in accepted_tuples]
    else:
        accepted_tuples = []
    
    for out_folder in sorted(os.listdir(output)):
        out_folder = os.path.join(output, out_folder)
        print("looking in ", out_folder)
        
        iterator = iter(sorted(os.listdir(out_folder)))
        curr_img_name = next(iterator)
        try:
            while(True):
                curr_img_path = os.path.join(out_folder, curr_img_name)
                curr_img = np.array(Image.open(curr_img_path))
                
                ch_mean = np.mean(np.var(curr_img, axis=(0,1)))
                
                if ch_mean < (7.79917553e+01 + 6.82441817e+01) / 2:
                    print("SPOTTED NOISY SCREEN:", curr_img_path, ch_mean)
                elif ch_mean < (7.79917553e+01 + 6.82441817e+01) / 2 * 3:
                    print("MAYBE NOISY SCREEN:", curr_img_path, ch_mean)
                
                next_img_name = next(iterator)
                next_img_path = os.path.join(out_folder, next_img_name)
                next_img = np.array(Image.open(next_img_path).resize(curr_img.shape[:2], Image.ANTIALIAS))
                
                distance = np.sum((curr_img - next_img)**2)
                
                if (curr_img_name, next_img_name) not in accepted_tuples:
                    if distance < 2000000:
                        print("SPOTTED REPETITION:", curr_img_path, next_img_path, distance)
                    elif distance < 2000000 * 3:
                        print("MAYBE REPETITION:", curr_img_path, next_img_path, distance)
                        
                curr_img_name = next_img_name
        except StopIteration:
            continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parses command.'
    )
    parser.add_argument('--folder', dest='output', required=True)
    parser.add_argument('--accepted_tuples', dest='accepted_tuples', action='store_true')
    main(**vars(parser.parse_args()))