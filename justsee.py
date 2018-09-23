import __main__
__main__.pymol_argv = ['pymol','-q']
import pymol
import sys, time, os


# Haemoglobin in this example illustrates careful use of selection algebra
pymol.cmd.load("2HHB.pdb")

# create objects for alpha1, beta1 and alpha1,beta1 pair of subunits
pymol.cmd.create("alpha1", "2HHB and chain A")
pymol.cmd.create( "beta1", "2HHB and chain B")
pymol.cmd.create("ab1", "2HHB and chain A+B")

# get hydrogens onto everything (NOTE: must have valid valences on e.g. small organic molecules)
pymol.cmd.h_add

# make sure all atoms within an object occlude one another
#pymol.flag ignore, none

# use solvent-accessible surface with high sampling density
pymol.cmd.set("dot_solvent", 1)
pymol.cmd.set("dot_density", 3)

# measure the components individually storing the results for later
alpha1_area=pymol.cmd.get_area("alpha1")
beta1_area=pymol.cmd.get_area("beta1")


# measure the alpha1,beta1 pair
ab1_area=pymol.cmd.get_area("ab1")

# now print results and do some maths to get the buried surface
print alpha1_area
print beta1_area
print ab1_area
print (alpha1_area + beta1_area) - ab1_area