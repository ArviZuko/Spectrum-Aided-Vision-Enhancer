import numpy as np
import cv2
import os






#NBI for Capsule
table1 = np.load('cap1.npy')
table2 = np.load('cap3_2.npy')
table3 = np.load('cap5.npy')

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

def to_nbi(wli, is_dual = False):
    h,w,c = wli.shape

    image_rgb = cv2.cvtColor(wli, cv2.COLOR_BGR2RGB)

    pred_img2 = transfer_by_table(image_rgb, table2)

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

src_path = r'D:\SRGAN\VCE\data_VCE\hr_images'
tar_path = r'D:\SRGAN\VCE\data_VCE\lr_images'

res_files = get_all_ext_list(src_path, 'png')

is_dual = False

for index, file in enumerate(res_files):
    
    dump_file = file.replace(src_path, tar_path)
    dump_file_path = os.path.dirname(os.path.abspath(dump_file))
    
    if not os.path.isdir(dump_file_path):
        try:
            os.makedirs(dump_file_path)
        except FileExistsError:
            print("建立路徑異常。")
            
    img = cv2.imread(file)
#     img = img[22:922, 694:1894,:]
    nbi = to_nbi(img, is_dual=is_dual)
    
    cv2.imwrite(dump_file, nbi)
    
    #print(index, dump_file)