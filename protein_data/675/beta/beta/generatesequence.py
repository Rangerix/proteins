from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import three_to_one
from Bio.PDB.Polypeptide import is_aa
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import sys,numpy

#=======================================================================================================
def getfreq (str):
	#alphabet=['a','c','d','e','f','g','h','i','k','l','m','n','p','q','r','s','t','v','w','y']
	eliminate=['b','j','o','u','x','z']
	alphabet="ACDEFGHIKLMNPQRSTVWY"
	freq=[ 0 for _ in range(26) ]
	for i in str:
		freq[ord(i)-ord('A')]+=1
	#print(freq)
	return freq

#=======================================================================================================
infile=sys.argv[1]
outfile=sys.argv[2]
alphabet="ACDEFGHIKLMNPQRSTVWXY"
with open(outfile,"a") as f:
	f.write("id"+'\t')
	for i in alphabet:
		f.write(i+'\t')
	f.write('\n')
with open(infile) as f1:
	pdblist=f1.read().splitlines()

for pdbid in pdblist:
	pdbFile = pdbid+".pdb"

	## First, open and parse the protein file
	p = PDBParser(PERMISSIVE=1)
	structure = p.get_structure(pdbFile, pdbFile)
	print(pdbid)
	for model in structure:
		for chain in model:
			seq = list()
			chainID = chain.get_id()
			 
			for residue in chain:
				if is_aa(residue.get_resname(), standard=True):
					seq.append(three_to_one(residue.get_resname()))
				else:
					seq.append("X")
			 
			chainseq=str("".join(seq))
			#print(">Chain_" + chainID + "\n" + str("".join(seq)))
			#print(chainseq)
			dict1=getfreq(chainseq)
			#print(dict1)
			alphabet="ACDEFGHIKLMNPQRSTVWXY"
			indices=[]
			dict2=numpy.array(dict1)
			for i in alphabet:
				index=ord(i)-ord('A')
				indices.append(ord(i)-ord('A'))
			indices2=numpy.array(indices)
			res=(dict2[indices2])
			#print(res)
			
			with open(outfile,"a") as f:
				f.write(pdbid+'\t')
				for i in res:
					f.write(str(i)+'\t')
				f.write('\n')
		