import cv2
import os
import os.path
import glob
import numpy as np
import string

targets = "E:\\Work\\Paper\\Thesis Paper\\A Novel Narrow Band Conversion Technique using Hyperspectral Imaging for Capsule Endoscopy\\20230314_NBI progress Data\\Data\\Olympus\\Olympus_nbi_simulated\\11.jpg"
sources = glob.glob("E:\\Work\\Paper\\Thesis Paper\\A Novel Narrow Band Conversion Technique using Hyperspectral Imaging for Capsule Endoscopy\\20230314_NBI progress Data\\Data\\Olympus\\Olympus_wli"+"/*.jpg")

def read_file( sn, tn):
        s = cv2.imread(sn)
        s = cv2.cvtColor(s,cv2.COLOR_BGR2LAB)
        t = cv2.imread(tn)
        t = cv2.cvtColor(t,cv2.COLOR_BGR2LAB)
        return s, t

def get_mean_and_std(x):
    x_mean, x_std = cv2.meanStdDev(x)
    x_mean = np.hstack(np.around(x_mean,2))
    x_std = np.hstack(np.around(x_std,2))
    return x_mean, x_std

for n in range(len(sources)):
    print("Converting picture"+str(n+1)+"..."+sources[n])
    s, t = read_file(sources[n],targets)
    height, width, channel = s.shape
    theight, twidth, tchannel = t.shape
    if((height!=theight) or (width!=twidth)):
         t = cv2.resize(t, (height,width))
         
    s_mean, s_std = get_mean_and_std(s)
    t_mean, t_std = get_mean_and_std(t)
    
    for i in range(0,height):
        for j in range(0,width):
            for k in range(0,channel):
                x = s[i,j,k]
                x = ((x-s_mean[k])*(t_std[k]/s_std[k]))+t_mean[k]
                # round or +0.5
                x = round(x)
                # boundary check
                x = 0 if x<0 else x
                x = 255 if x>255 else x
                s[i,j,k] = x
    s = cv2.cvtColor(s,cv2.COLOR_LAB2BGR)
    op_name = sources[n].split("\\")
    cv2.imwrite("E:\\Work\\Paper\\Thesis Paper\\Assessment of Narrow Band Imaging Algorithm for Video Capsule Endoscopy Based on Decorrelated Color Space for Esophageal Cancer\\Data\\color\\"+op_name[-1]+'.bmp',s)

