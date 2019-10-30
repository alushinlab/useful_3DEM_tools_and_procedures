# Create soft circular masks
This directory contains the code necessary to generate custom soft masks in 2D.
To run this software, it is recommended that the anaconda environment matt_EMAN2 is installed and active.
This environment can be found in the main directory of this repository. If one opts to not have this environment
active, then the current python installation must have the following libraries installed: matplotlib, numpy, skimage, and mrcfile.

Additionally, this software requires that one have a working installation of SPIDER (https://spider.wadsworth.org/spider_doc/spider/docs/spider-inst-linux.html) and eman1 (https://blake.bcm.edu/emanwiki/EMAN1/Install). 

To make a custom circular mask, the make_soft_mask.py script can be run in the command line as follows (minimal arguments):
```
./make_soft_mask.py --box_len=512 --radius=125 --falloff_width=50
```
Where:
- box_len = The length of the image in pixels. The generated mask will always be a square image.
- radius = The radius of the circular mask in pixels. Note that this is the radius, not the diameter.
- falloff_width = The width of the cosine-shaped falloff outside of the mask range.

In addition to this minimum run, there are several features that may optionally be specified to allow for further customization:
```
./make_soft_mask.py --box_len=512 --radius=125 --falloff_width=50 --xcent=100 --ycent=170 --keep_hard=True
```
Where:
- box_len = The length of the image in pixels. The generated mask will always be a square image.
- radius = The radius of the circular mask in pixels. Note that this is the radius, not the diameter.
- falloff_width = The width of the cosine-shaped falloff outside of the mask range.
- xcent = x-coordinate of the center of the circle. Default is half the box_len.
- ycent = y-coordinate of the center of the circle. Default is half the box_len.
- keep_hard = Boolean value that specifies if you would like to keep the hard circular mask or delete it.
- show_masks = Boolean value that specifies if you would like to display the hard and soft masks as they are created. If set to False, matplotlib is not a required library.
