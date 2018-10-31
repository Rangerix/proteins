import numpy
from scipy.stats import skew,kurtosis
from Bio.PDB.PDBParser import PDBParser
from Bio import PDB                    
import warnings
from Bio import BiopythonWarning
import sys
import os
warnings.simplefilter('ignore', BiopythonWarning)                                   
parser = PDBParser(PERMISSIVE=1)

infilename =sys.argv[1]
with open(infilename) as myfile:
	pdbidlist=myfile.read().splitlines()
outfile=sys.argv[2]
myfile=open(outfile,'a')
for pdbid in pdbidlist:
	structure_id = pdbid
	filename=structure_id+".pdb"
	skewval=100
	kurtval=100
	if (os.path.isfile(filename)):
		structure = parser.get_structure(structure_id, filename)
		#skewness can be measured either only for CA atoms or all atoms present in the protein
		#first I'm doing for CA atoms

		#idea 1: measure skewness for each chain; then take average
		#for each chain, we can use two ways to measure kurtosis
		#idea 1.1: measure kurtosis for x,y and z coodinates seperately, then take average
		skewchain=[]
		kurtchain=[]
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
				avgskew=(xskew+yskew+zskew)/3
				#===
				xkurt=kurtosis(xvalues)
				ykurt=kurtosis(yvalues)
				zkurt=kurtosis(zvalues)
				avgkurt=(xkurt+ykurt+zkurt)/3
				#print(avg)
				skewchain.append(avgskew)
				kurtchain.append(avgkurt)
		skewval=numpy.mean(skewchain)
		kurtval=numpy.mean(kurtchain)
		#print(structure_id,skewval,kurtval)
		
	myfile.write(structure_id+'\t')
	myfile.write(str(skewval)+'\t')
	myfile.write(str(kurtval)+'\n')

		
