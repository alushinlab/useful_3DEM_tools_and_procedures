# useful_tools
This repository contains useful tools for image processing.
One tool that may be useful if one wants to compute Fourier ring correlation curves is the create_masks.py script. When calculating FRCs, it may be useful to first mask inputs with a circular maskto prevent noise at the edge of the image affecting the FRC curve. However, using a hard mask can cause artifacts in the high resolution range. This script allows one to create a custom, soft, circular mask. Details on how to run the script may be found in its [README](./FRC_calcs/create_masks_README.md).
