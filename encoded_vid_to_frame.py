import os
import re

files = os.listdir("C:\\Users\\Furkan\\Desktop\\BLG4901E\\nii_deney\\post_enc_vids2")
frame_folders_path = "C:\\Users\\Furkan\\Desktop\\BLG4901E\\nii_deney\\post_enc_frames2"
    
for i, file in enumerate(files):
    os.system(f"mkdir {frame_folders_path}\\{file[:-4]}")
    command = f"ffmpeg -f rawvideo -framerate 25 -s 256x256 -pixel_format yuv420p -i post_enc_vids2\\{file} -c copy -f segment -segment_time 0.04 post_enc_frames2\\{file[:-4]}\\encoded_image%3d.yuv"
    os.system(command)
    
    
    
    