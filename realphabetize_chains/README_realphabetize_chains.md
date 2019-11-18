# Realphabetize chains
When morphing between coordinate files in UCSF Chimera or Pymol, it is necessary that cooresponding chains have the same 
alphanumeric chain ID. We wrote this script so that when we fit subunits into maps, the chain indices between different
coordinate files was consistent. 

The realphabetize_chains.py script will rename the chains in a given PDB file to be in alphabetical order along the z-axis. 
The subunit whose centroid is the highest in the Z dimension will be 'A'

To run this software, it is recommended that the anaconda environment matt_EMAN2 is installed as recommended
[here](../conda_env/conda_env_README.md). If one opts to not have this environment, then the current python installation must have
the following libraries installed: numpy, and prody.

The realphabetize_chains.py script can be run in the command line as follows (minimal arguments):
```
./realphabetize_chains.py -i my_pdb_file.pdb
```
Where:
- i = input file name of coordinate file; must be .pdb file

The output of this script will be a .pdb file with the name my_pdb_file_renamedChains.pdb

In addition to this minimum run, the output file name may be specified:
```
./realphabetize_chains.py -i my_pdb_file.pdb -o alphabetized_coord_file.pdb
```
Where:
- i = input file name of coordinate file; must be .pdb file
- o = output file name of coordinate file with renamed chains; optional; must be .pdb file

The output of this script will be a .pdb file with the name alphabetized_coord_file.pdb
