#!/mnt/data1/Matt/anaconda_install/anaconda2/envs/matt_EMAN2/bin/python
################################################################################
# import some python packages
import numpy as np
from skimage.draw import circle
import mrcfile
import subprocess
################################################################################
# Specify inputs
import argparse; import sys
parser = argparse.ArgumentParser('Generate circular mask files.')
parser.add_argument('--box_len', type=int, help='length of your square image, in pixels; required')
parser.add_argument('--radius', type=float, help='circle radius; required')
parser.add_argument('--falloff_width', type=float, help='Falloff width of cosine mask; required')
parser.add_argument('--xcent', type=float, help='x-coordinate of center of circle. Default is half box_len')
parser.add_argument('--ycent', type=float, help='y-coordinate of center of circle. Default is half box_len')
parser.add_argument('--keep_hard', type=str, help='True to keep hard mask, False to delete hard mask. Default is True')
parser.add_argument('--show_masks', type=str, help='True to show masks, False to not show masks. Default is True')
args = parser.parse_args()
print('')
if(args.box_len == None):
	print('The box length of the image was not specified.')
	sys.exit('The preferred input style may be found with ./projection_generator.py -h')

if(args.radius == None):
	print('The radius of the circular mask was not specified.')
	sys.exit('The preferred input style may be found with ./projection_generator.py -h')

if(args.falloff_width == None):
	print('The falloff width of the soft mask was not specified.')
	sys.exit('The preferred input style may be found with ./projection_generator.py -h')

if(args.xcent == None or args.ycent == None):
	print('You did not specify the center coordinates of the circle. The circle will be centered in the image.')

print('Hard and soft 2D masks will now be generated to your specifications')
################################################################################
# Store the inputs as local variables
box_len = args.box_len
radius = args.radius
falloff = args.falloff_width
if(args.xcent == None): xcent = box_len/2.0
else: xcent = args.xcent
if(args.ycent == None): ycent = box_len/2.0
else: ycent = args.ycent

if(args.keep_hard == None): 
	keep_hard = True
elif (args.keep_hard.lower() in ('yes', 'true', 't', 'y', '1')):
	keep_hard = True
else: keep_hard = False

if(args.show_masks == None): 
	show_masks = True
elif (args.show_masks.lower() in ('yes', 'true', 't', 'y', '1')):
	show_masks = True
else: show_masks = False

################################################################################
# Generate a temporary file to run a spider procedure
proc_string = 'CP FROM MRC\ncirc_mask_hard.mrc\ncirc_mask\nN\nMA SOFT\ncirc_mask\ncirc_mask_soft\nC\n0.5\n%d\nEN D\n\n'%falloff
spi_proc_file = open('spider_procedure.spi', 'w')
spi_proc_file.write(proc_string)
spi_proc_file.close()

# Make the circle
img = np.zeros((box_len,box_len))
rr, cc = circle(xcent,ycent,radius)
img[rr,cc] = 1

if(show_masks):
	import matplotlib.pyplot as plt
	plt.imshow(img, cmap=plt.cm.gray)
	plt.show()

with mrcfile.new('circ_mask_hard.mrc', overwrite=True) as mrc:
	mrc.set_data(img.astype('float32'))

# Run the spider procedure and convert soft mask to mrc file
subprocess.call(['spider', 'spi', '@spider_procedure'])
subprocess.call(['proc2d' ,'circ_mask_soft.spi', 'circ_mask_soft.mrc', 'mrc'])
# Remove temporary files
subprocess.call(['rm', 'circ_mask.spi']) 
subprocess.call(['rm', '.emanlog', 'circ_mask_soft.spi', 'spider_procedure.spi'])
if(not keep_hard):
	subprocess.call(['rm', 'circ_mask_hard.mrc'])

# Lastly, plot the final mask, if specficied by the user
if(show_masks):
	with mrcfile.open('circ_mask_soft.mrc') as mrc:
		img = mrc.data
	plt.imshow(img, cmap=plt.cm.gray)
	plt.show()



