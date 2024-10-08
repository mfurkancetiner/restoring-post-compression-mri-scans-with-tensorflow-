+ The dataset used with this model is from [this](https://biomedic.doc.ic.ac.uk/brain-development/downloads/IXI/) (3.8G one) website and it consists of 256x256 mri scan slices <br/>
+ Versatile Video Coding was used to lossy compress and decompress images to create noise, which I tried to mitigate with this model. <br/>
+ FFmpeg was used to convert the slices to a 3D YUV video format so they could be used for VVC <br/>
+ Python scripts are available for both (nii to frame -> frame to vid -> vid enc and dec -> encoded vid to frame )
+ The original model is from [this](https://www.mdpi.com/2076-3417/11/17/7803) paper but I processed the images in 3D instead of 2D, as an experiment. <br/>
+ Model was trained on 460 patients' data (with 128 slices from each) for 15 epochs and validated on 104. <br/>
+ The average PSNR score was increased from 30.13 to 32.97, meaning a 2.84 score increase <br/>
+ The model takes about 14GBs of GPU size to run with my configurations



