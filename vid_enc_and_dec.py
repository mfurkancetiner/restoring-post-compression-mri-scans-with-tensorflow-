import os
import re

pre_enc_files = os.listdir("pre_enc_vids2")

encode_command = ("c:/users/furkan/desktop/blg4901e/vvenc/bin/debug-static/vvencFFapp --preset medium --InternalBitDepth 8"
        " --TargetBitrate 170000 --Size 256x256 -fr 25")
                
for i, file in enumerate(pre_enc_files):
    if i <= 520:
        continue
    os.system(encode_command + (
    f" --InputFile C:/Users/Furkan/Desktop/BLG4901E/nii_deney/pre_enc_vids2/{file}" 
    f" --BitstreamFile=C:/Users/Furkan/Desktop/BLG4901E/nii_deney/p266/{file[:-4]}.266")
    )


decode_command = "c:/users/furkan/desktop/blg4901e/vvdec/bin/debug-static/vvdecapp -b" 

h266_files = os.listdir("p266")
for i, file in enumerate(h266_files):
    os.system(decode_command +(
    f" C:/Users/Furkan/Desktop/BLG4901E/nii_deney/p266/{file} -o"
    f" C:/Users/Furkan/Desktop/BLG4901E/nii_deney/post_enc_vids2/{file[:-4]}_encoded.yuv")
    )
