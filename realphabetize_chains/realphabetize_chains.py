#!/mnt/data1/Matt/anaconda_install/anaconda2/envs/tf-gpu/bin/python
# Import python files
print('')
print('Loading packages...')
import numpy as np
from prody import *
import string
print('Packages loaded')
################################################################################
# Parse inputs
import argparse; import sys
parser = argparse.ArgumentParser('Rename protein chains in PDB file based on z-axis position.')
parser.add_argument('-i', type=str, help='input file name of coordinate file; must be .pdb file')
parser.add_argument('-o', type=str, help='output file name of coordinate file with renamed chains; optional; must be .pdb file')
args = parser.parse_args()
print('')
if(args.i == None):
	print('The input file name was not specified.')
	sys.exit('The preferred input style may be found with ./realphabetize_chains.py -h\n')

if(not (args.i[-4:] == '.pdb')):
	print('Please specify a .pdb file as input')
	sys.exit('The preferred input style may be found with ./realphabetize_chains.py -h\n')

if(args.o != None):
	if(not(args.o[-4:] == '.pdb')):
		print('An improper output file name was given. This parameter will be ignored')
		args.o = None
################################################################################
# Store the inputs as local variables
file_name = args.i
output_file_name = args.o
if(output_file_name == None): 
	output_file_name = file_name[:-4] + '_renamedChains.pdb'
	print('No output file name was specified. The renamed pdb file will be '+output_file_name)

print('Loading PDB and renaming chains')
p = parsePDB(file_name)
chids = set(p.getChids())
chains = []
for chain_idx in chids:
	chains.append(p.select('chain ' + chain_idx).copy())

# get the coordinates for each atom of each actin subunit
coords = []
for i in range(0,len(chains)):
	coords.append(chains[i].getCoords())

# make each helix into a [num_chains x num_atoms_per_actin x 3] array
coords = np.asarray(coords)
centroids = np.average(coords, axis=1)
center = np.average(centroids, axis=0)
centroids = centroids - center

z_index = np.argsort(centroids[:,2])
new_chain = []
for i in range(0,len(chains)):
	temp = chains[z_index[i]].copy()
	temp.setChids(string.ascii_uppercase[i])
	new_chain.append(temp)

p_new = new_chain[0]
for i in range(1, len(new_chain)):
	p_new = p_new + new_chain[i]

print('Chains renamed.')
print('Saving output file as ' + output_file_name)
writePDB(output_file_name, p_new)
print('File saved. Exiting...\n')
