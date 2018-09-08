#this is to calculate accessible surface area for a pdb file
#this file takes a file with list of pdbids and an output filename
#the pdb files must be downloaded in the same directory
#output foemat: pdbid area

from __future__ import print_function
import __main__
__main__.pymol_argv = ['pymol','-q']
import pymol
import sys, time, os

pymol.finish_launching()


infilename =sys.argv[2]
outfilename=sys.argv[3]
#pdbid="1fat"
with open(infilename) as myfile:
	pdbidlist=myfile.read().splitlines()

for pdbid in pdbidlist:
	print(pdbid)
	pymol.cmd.delete("all")
	pymol.cmd.load(pdbid+".pdb")

	# get hydrogens onto everything (NOTE: must have valid valences on e.g. small organic molecules)
	pymol.cmd.h_add

	# make sure all atoms within an object occlude one another
	pymol.cmd.flag ("ignore", "none")

	# use solvent-accessible surface with high sampling density
	pymol.cmd.set("dot_solvent", 1)
	pymol.cmd.set("dot_density", 3)

	# measure the components individually storing the results for later
	sum=0.0
	chn_list=[]
	chn_list=pymol.cmd.get_chains()
	#print chn_list
	overall= '+'.join(chn_list)
	for i in chn_list:
		val=pdbid.upper()+" and chain "+i
		print(val,end=' ')
		name="alpha"+i
		pymol.cmd.create(name,val)
		tmp_area=pymol.cmd.get_area(name)
		print (tmp_area)
		sum=sum+tmp_area

	#print (sum)

	val=pdbid.upper()+" and chain "+ overall
	pymol.cmd.create("alpha",val)
	tmp_area=pymol.cmd.get_area("alpha")
	#print (tmp_area)

	asa=(sum-tmp_area)
	print (asa)

	with open(outfilename,"a") as myfile:
		myfile.write(pdbid+" "+str(asa)+"\n")
	print("\n\n")

pymol.cmd.quit()