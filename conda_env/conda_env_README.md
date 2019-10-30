The software in the Alushin lab using Python is primarily developed in an anaconda environment that has many packages installed 
that are useful for image processing, interfacing with various 3DEM softwares, and deep learning. 

You may notice that the top line of each Python script points to that environment. If you would like to run any Python-based
scripts from the Alushin lab, it is generally recommended to install that environment in an anaconda installation to ensure 
everything runs smoothly. To do so, first download the anaconda environment [here]().

To setup the environment on your local computer, create a new conda environment by navigating to the downloaded .yml and 
entering the following command:
```
conda env create -f matt_EMAN2.yml
```
After installation, to run any scripts that use this environment, it is recommended to create a symbolic link to the python 
version in this environment so that you may easily run any scripts from the Alushin lab. 
```
ln -s /path_to_this_env/bin/python /mnt/data1/Matt/anaconda_install/anaconda2/envs/matt_EMAN2/bin/python
```
Alternatively, you may change the first line of every script to point to the correct python installation. Once this is complete,
you should be able to run most of the Alushin lab software using this package. 
