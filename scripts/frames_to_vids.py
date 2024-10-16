import os
import re

folder_path = "C:/Users/Furkan/Desktop/BLG4901E/nii_deney/pre_enc_frames"
os.chdir(folder_path)
folders = os.listdir(folder_path)

for i, folder in enumerate(folders):
    os.chdir(f'C:/Users/Furkan/Desktop/BLG4901E/nii_deney/pre_enc_frames/{folder}')
    pattern = re.compile(r'image\d{3}\.yuv')
    files = os.listdir(os.getcwd())
    
    matching_files = [file for file in files if pattern.match(file)]

    file_names = f"concat:{matching_files[0]}"
    for file in matching_files[1:]:
        file_names+= "|" + file
        
    command = 'ffmpeg -s:v 256x256 -r 25 -i ' + '"' + file_names + '"' + f' -c:v rawvideo -pix_fmt yuv420p C:/Users/Furkan/Desktop/BLG4901E/nii_deney/pre_enc_vids2/{folder}.yuv'
    
    os.system(command)
