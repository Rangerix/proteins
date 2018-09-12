import numpy
from scipy.stats import skew
from Bio.PDB.PDBParser import PDBParser
from Bio import PDB                    
import warnings
from Bio import BiopythonWarning
import sys

warnings.simplefilter('ignore', BiopythonWarning)                                   
parser = PDBParser(PERMISSIVE=1)

infilename =sys.argv[1]
with open(infilename) as myfile:
	pdbidlist=myfile.read().splitlines()


for pdbid in pdbidlist:
	structure_id = pdbid
	filename=structure_id+".pdb"
	structure = parser.get_structure(structure_id, filename)
	print(structure_id)
	#skewness can be measured either only for CA atoms or all atoms present in the protein
	#first I'm doing for CA atoms

	#idea 1: measure skewness for each chain; then take average
	#for each chain, we can use two ways to measure kurtosis
	#idea 1.1: measure kurtosis for x,y and z coodinates seperately, then take average
	skewchain=[]
	for model in structure.get_list():
		for chain in model.get_list():
			xvalues=[]
			yvalues=[]
			zvalues=[]
			for residue in chain.get_list():
				if residue.has_id("CA"):
					ca=residue["CA"]
					#print(ca.get_coord())
					temp=ca.get_coord()
					#print(temp[0])
					xvalues.append(temp[0])
					yvalues.append(temp[1])
					zvalues.append(temp[2])

			#print(chain)
			xskew=skew(xvalues)
			yskew=skew(yvalues)
			zskew=skew(zvalues)
			avg=(xskew+yskew+zskew)/3
			#print(avg)
			skewchain.append(avg)
	print("chainwise average : ",numpy.mean(skewchain))
	#idea 1.2: (xi - meanx)^3+(yi - meany)^3+(zi - meanz)^3/sdx+sdy+sdz

	#idea 2: measure skewness for all CA atoms present
	xvalues=[]
	yvalues=[]
	zvalues=[]
	for model in structure.get_list():
		for chain in model.get_list():
			for residue in chain.get_list():
				if residue.has_id("CA"):
					ca=residue["CA"]
					#print(ca.get_coord())
					temp=ca.get_coord()
					#print(temp[0])
					xvalues.append(temp[0])
					yvalues.append(temp[1])
					zvalues.append(temp[2])
	xskew=skew(xvalues)
	yskew=skew(yvalues)
	zskew=skew(zvalues)
	avg=(xskew+yskew+zskew)/3
	print("all put together : ",avg)