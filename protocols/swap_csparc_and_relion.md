# Switching back and forth between cryosparc and RELION

This document describes the way that we typically swap between cryosparc and RELION. The exact commands vary based on the stage of 
processing, but commonly used protocols are outlined below. 

## RELION to cryosparc after particle extraction/subset selection: 
- Navigate to the relion directory
- Check the existence of your particles.star file; i.e. `ls Extract/job005` or `ls Select/job007`
- Combine all of your extracted/selected particles into a single .mrcs stack and associated star file. Change 'full_particle_stack' 
to whatever path/file prefix you would like. This will produce as output full_particle_stack.star and full_particle_stack.mrcs 
in your main relion directory.
```
relion_preprocess --operate_on Select/job007/particles.star --operate_out full_particle_stack
```
- In the appropriate Project and Workspace in cryosparc where you would like to operate on the particles, make a new job using 
Job Builder >> Import Particle Stack
- For the 'Particle meta path' field, enter the full path to full_particle_stack.star
- For the 'Particle data path' field, enter the full path to full_particle_stack.mrcs
- Leave all other fields as blank and queue the job
- You should now have your particles imported to cryosparc for 2D classification, ab initio model generation etc.

***
## Cryosparc to RELION after some type of 3D refinement;
- In the command line interface, navigate to your refinement job; i.e. `cd csparc/P1/J3`
- Identify the .cs file that contains the information you would like in your new star file, and know the paths to your imported particles
- Use the [csparc2star.py script from pyem](https://github.com/asarnow/pyem/blob/master/csparc2star.py) to convert your .cs 
file into a .star file. 
```
csparc2star.py cryosparc_P1_J3_003_particles.cs output_particles.star --stack-path /path_to_imported_particles/full_particle_stack.mrcs --copy-micrograph-coordinates /path_to_imported_particles/full_particles.star
```
Where the first input is the final particles.cs file from your refinement, the second output is the name of the output star file.
Note the two extra parameters '--stack-path' and '--copy-micrograph-coordinates' are necessary to maintain information about 
where the particles were extracted from. These fields are necessary if you would like to do analysis on inter-particle distances
or any type of per-particle CTF refinement or Bayesian polishing.
- You may now use this star file as input for RELION 2D/3D classification or 3D refinement.
