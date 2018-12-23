from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import three_to_one
from Bio.PDB.Polypeptide import is_aa
from Bio.Alphabet import IUPAC
from collections import Counter
from Bio import SeqIO
import sys,numpy
import regex as re
import collections

#-------------------------------------------------------------------------------------------------
def getfreq (tmpstr):
	#alphabet=['a','c','d','e','f','g','h','i','k','l','m','n','p','q','r','s','t','v','w','y']
	#alphabet=[ABCDEF]*[ABCDEF]
	alphabet=["AA","BA","CA","DA","EA","FA","AB","BB","CB","DB","EB","FB","AC","BC","CC","DC","EC","FC","AD","BD","CD","DD","ED"
	,"FD","AE","BE","CE","DE","EE","FE","AF","BF","CF","DF","EF","FF"]
	eliminate=['b','j','o','u','x','z']
	#alphabet="ACDEFGHIKLMNPQRSTVWY"
	freq={ i:0 for i in alphabet }
	for i in alphabet:
		freq[i]=(len(re.findall(i, tmpstr,overlapped=True)))

	#print(freq)
	#sortedfreq = collections.OrderedDict(sorted(freq.items()))
	return freq
#------------------------------------------------------------------------------------


def convert_exchange(tmpstr):
	#A = {H, R, K}, B = {D, E, N, Q}, C = {C}, D = {S, T, P, A, G},
	#E = {M, I, L, V}, F = {F, Y, W}
	
	tmpstr=tmpstr.replace('H','A')
	tmpstr=tmpstr.replace('R','A')
	tmpstr=tmpstr.replace('K','A')
	
	tmpstr=tmpstr.replace('D','B')
	tmpstr=tmpstr.replace('E','B')
	tmpstr=tmpstr.replace('N','B')
	tmpstr=tmpstr.replace('Q','B')

	tmpstr=tmpstr.replace('C','C')

	tmpstr=tmpstr.replace('S','D')
	tmpstr=tmpstr.replace('T','D')
	tmpstr=tmpstr.replace('P','D')
	tmpstr=tmpstr.replace('A','D')
	tmpstr=tmpstr.replace('G','D')

	tmpstr=tmpstr.replace('M','E')
	tmpstr=tmpstr.replace('I','E')
	tmpstr=tmpstr.replace('L','E')
	tmpstr=tmpstr.replace('V','E')

	tmpstr=tmpstr.replace('F','F')
	tmpstr=tmpstr.replace('Y','F')
	tmpstr=tmpstr.replace('W','F')

	#print(tmpstr)
	return tmpstr
#------------------------------------------------------------------------------------------------------

outfile=sys.argv[2]
infile=sys.argv[1]
alphabet=["AA","BA","CA","DA","EA","FA","AB","BB","CB","DB","EB","FB","AC","BC","CC","DC","EC","FC","AD","BD","CD","DD","ED"
	,"FD","AE","BE","CE","DE","EE","FE","AF","BF","CF","DF","EF","FF"]
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
			tmpstr=convert_exchange(chainseq)
		
			dict1=getfreq(tmpstr)
			#print(dict1)
			#dict2=Counter(dict1)+Counter(dict2)
			'''
			dict2=numpy.add(dict2,dict1)
			print("")
			'''


			#print(dict2)
			res=[]
			for i in alphabet:
				#print(i,dict2[i],end='\t')
				res.append(dict1[i])
			print()
			#resarr=numpy.array(res)
			with open(outfile,"a") as f:
				f.write(pdbid+'\t')
				for i in res:
					f.write(str(i)+'\t')
				f.write('\n')
