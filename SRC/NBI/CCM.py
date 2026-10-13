import numpy as np
import cv2
import pillow
from colorthief import ColorThief

color_thief = ColorThief('3.bmp')
dominant_color = color_thief.get_color(quality=1)
palette = color_thief.get_palette(color_count=6)
"""
m_2 = [[67, 71, 58],
       [119, 121, 101],
       [98, 138, 114],
       [90, 69, 56],
       [115, 167, 143],
       [156, 147, 123],
       [97, 65, 54],
       [92, 160, 136],
       [80, 113, 92],
       [60, 114, 93],
       [168, 93, 75],
       [143, 73, 59],
       [54, 122, 100],
       [132, 85, 69],
       [60, 68, 56],
       [166, 79, 64],
       [80, 154, 130],
       [108, 135, 112],
       [168, 179, 154],
       [151, 167, 124],
       [135, 152, 128],
       [96, 113, 92],
       [65, 78, 63],
       [47, 57, 47]]

m_1 = [[34, 40, 55],
       [13, 46, 46],
       [29, 59, 50],
       [40, 55, 44],
       [21, 42, 63],
       [7, 90, 44],
       [58, 53, 54],
       [16, 35, 59],
       [52, 40, 49],
       [28, 48, 52],
       [23, 115, 23],
       [59, 79, 40],
       [21, 43, 49],
       [15, 79, 30],
       [51, 46, 68],
       [54, 117, 28],
       [39, 30, 62],
       [10, 50, 44],
       [39, 103, 75],
       [30, 82, 59],
       [23, 67, 49],
       [21, 50, 43],
       [29, 55, 53],
       [37, 64, 61]]

def main(m_1, m_2, rcond='None'):
    global ccm
    ccm = np.linalg.lstsq(m_1, m_2)[0]
    print(ccm)
main(m_2, m_1, rcond='1')

def color_correction(img,ccm):
    global output
    window_name = 'image'
    img2 = img.reshape((img.shape[0] * img.shape[1], 3))
    output = np.matmul(img2, ccm)
    reshaped_back = output.reshape(img.shape).astype(img.dtype)
    cv2.imshow(window_name, reshaped_back)
    cv2.waitKey(0)
color_correction(img,ccm)
"""

