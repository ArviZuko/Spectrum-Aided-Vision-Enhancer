import numpy as np
import pandas as pd
import cv2
from matplotlib import pyplot as plt
from numpy.linalg import inv
import os
from os import listdir
from os.path import isfile, isdir, join
from os import walk
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf
import time

table_file = 'nor_wli_nbi_table.npy'
nbi_table = np.load(table_file)

def transfer_by_table(img, table):
    
    # reshape as nx3, and to int
    temp_img = img.reshape(-1, 3).astype(int)

    # transfer to table key
    img_keys = temp_img[:,0] + np.left_shift(temp_img[:,1], 8) + np.left_shift(temp_img[:,2], 16)

    # table mapping
    img_values = table[img_keys]

    # reconstruct to rgb image
    img_r = img_values.astype('uint8')
    img_g = np.right_shift(img_values, 8).astype('uint8')
    img_b = np.right_shift(img_values, 16).astype('uint8')

    img_trans = np.column_stack((img_r, img_g, img_b))

    img_trans = img_trans.reshape(img.shape)
    
    return img_trans

def filter_ext(files, tar_ext):
    
    tar_files = []
    
    for file in files:
        
        file_ext = os.path.splitext(file)[-1][1:].lower()
        
        if file_ext == tar_ext:
            tar_files.append(file)
        
    return tar_files
    
def get_all_ext_list(tar_path, tar_ext):
    
    all_tar_files = []
    
    for root, dirs, files in walk(tar_path):
        
        tar_files = filter_ext(files, tar_ext.lower())

        if len(tar_files) == 0:
            continue
            
        tar_files = [join(root, file) for file in tar_files]
            
        all_tar_files = all_tar_files + tar_files
        
    return all_tar_files

def wli_to_nbi(wli, trans_table, is_dual = False):
    
    h,w,c = wli.shape

    image_rgb = cv2.cvtColor(wli, cv2.COLOR_BGR2RGB)
    
    pred_img2 = transfer_by_table(image_rgb, trans_table)

    pred_img2 = cv2.cvtColor(pred_img2, cv2.COLOR_RGB2BGR)
    
    if is_dual:
        tar_img = np.zeros((h, w*2, c))
        tar_img[:h,:w,:] = wli
        tar_img[:h,w:2*w,:] = pred_img2
    else:
        tar_img = np.zeros((h, w, c))
        tar_img[:h,:w,:] = pred_img2
        
    tar_img = tar_img.astype('uint8')
    
    return tar_img

src_path = r'C:\Users\Arvind\Documents\WLI\test\ulcerative-colitis' 
tar_path = r'C:\Users\Arvind\Documents\SAVE\test\ulcerative-colitis'

tar_files = get_all_ext_list(src_path, 'jpg')

is_dual = False

table_file = 'nor_wli_nbi_table.npy'
nbi_table = np.load(table_file)

for index, file in enumerate(tar_files):
    
    dump_file = file.replace(src_path, tar_path)
    dump_file_path = os.path.dirname(os.path.abspath(dump_file))
    
    if not os.path.isdir(dump_file_path):
        try:
            os.makedirs(dump_file_path)
        except FileExistsError:
            print("建立路徑異常。")
            
    img = cv2.imread(file)
    nbi = wli_to_nbi(img, nbi_table, is_dual=is_dual)
    
    cv2.imwrite(dump_file, nbi)
