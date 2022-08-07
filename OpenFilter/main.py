"""
OpenFilter main code
Copyright (C) 2022  ELLIS Alicante Foundation

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

We explicly request to always consider the ethical implications 
of the technology and to avoid unethical uses or applications. 

EXCEPTION (dual license):

Users interested in using the code for commercial purposes are asked 
to contact the authors for an explicit authorization. The authors will
evaluate the ethical implications for each case.

contact information: piera@ellisalicante.org
"""


import random
import time
import numpy as np
import os
import argparse
from PIL import Image

import pyautogui as auto

positions = {
    "new_file": (1220,750),
    "many_cam": (1150,250),
    "many_cam_confirm": (1180,280),
    "screen": (42,305,510,510),
    "right_filter": (430,980),
    "left_filter": (150,980)
}

def drag_and_drop(start, end):
    auto.mouseDown(start)
    auto.moveTo(end)
    auto.mouseUp()

def sleep(ms):
    seconds = ms / 1000
    seconds += random.random()*seconds/10
    time.sleep(seconds)

def h_padding(img):
    background = Image.new('RGB', (img.size[0] + 5*img.size[0]//285, img.size[1]))
    background.paste(img, (background.size[0] - img.size[0], 0))
    return background

def v_padding(img):
    background = Image.new('RGB', (img.size[0], img.size[1] + 150*img.size[1]//285))
    background.paste(img, (0, (background.size[1] - img.size[1])//2))
    return background
    
def main(path, output, n_filters, move_right):
    filter = 0
    for img_folder in sorted(os.listdir(path)):
        print(img_folder)
        out_folder = os.path.join(output, img_folder)
        img_folder = os.path.join(path, img_folder)
        if not os.path.isdir(out_folder):
            os.makedirs(out_folder)
        if len(os.listdir(img_folder)) == len(os.listdir(out_folder)):
            filter += 1
            if filter == n_filters:
                filter = 0
            continue
        print("FILTER", filter)
        
        for iter, img_name in enumerate(sorted(os.listdir(img_folder))):
            out_path = os.path.join(out_folder, img_name)
            img_path = os.path.join(img_folder, img_name)
            if os.path.isfile(out_path):
                continue
            img = Image.open(img_path)
            img_size = img.size
            img = v_padding(h_padding(img))
            img.save(os.path.join("swapper", img_name))
            sleep(2000)
            if iter == 0:
                sleep(2000)
            drag_and_drop(positions["new_file"], positions["many_cam"])
            sleep(800)
            auto.click(positions["many_cam_confirm"])
            sleep(2000)
            screenshot = auto.screenshot(region=positions["screen"]).resize(img_size, Image.ANTIALIAS)
            screenshot.save(out_path)            
            os.remove(os.path.join("swapper", img_name))
        
        filter += 1
        if filter == n_filters:
            filter = 0
            if n_filters == 1:
                continue
            for _ in range(n_filters - 2):
                auto.click(positions["right_filter"] if not move_right else positions["left_filter"])
                sleep(3000)
            auto.click(positions["right_filter"] if not move_right else positions["left_filter"])
            sleep(20000)
        else:
            auto.click(positions["left_filter"] if not move_right else positions["right_filter"])
            sleep(20000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parses command.'
    )
    parser.add_argument('--dataset', dest='path', required=True)
    parser.add_argument('--output', dest='output', required=True)
    parser.add_argument('--n_filters', dest='n_filters', type=int, default=8)
    parser.add_argument('--move_right', dest='move_right', action='store_true')
    main(**vars(parser.parse_args()))
