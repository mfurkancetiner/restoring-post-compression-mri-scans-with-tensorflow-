import numpy as np
import nibabel as nib
import os

width, height = 256, 256

files = os.listdir("C:/Users/Furkan/Desktop/BLG4901E/nii_deney/data")

current_path = os.getcwd()
current_path = os.path.join(current_path, "pre_enc_frames2")

for file in files:
    file = "data/" + file 
    image = nib.load(file).get_fdata()
    yuv_frames = []

    frames_path = os.path.join(current_path, file[5:-7])
    
    if(os.path.isdir(frames_path) == 0):
        os.system(f"mkdir {frames_path}")

    for i in range(image.shape[2]):
        test = image[:,:,i]
        norm = np.zeros((test.shape[0], test.shape[1]), dtype=np.uint8)

        min = 800
        max = 0
        for row in range(test.shape[0]):
            for col in range(test.shape[1]):  
                x = test[row][col]      
                if x < min:
                    min = x
                elif x > max:
                    max = x
                
        for row in range(test.shape[0]):
            for col in range(test.shape[1]):
                x = round(255 * ((test[row][col] - min) / (max - min)))
                norm[row][col] = x

        yuv_array = np.zeros((height + height //2 , width), dtype=np.uint8)

        yuv_array[:height, :] = norm
        yuv_array[height:, :width // 2] = 127
        yuv_array[height:, width // 2:] = 127
        
        with open(f"{frames_path}/image{i:03d}.yuv", "wb") as yuv_file:
            yuv_file.write(yuv_array.tobytes())
