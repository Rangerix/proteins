from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.Polypeptide import three_to_one
from Bio.PDB.Polypeptide import is_aa
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import sys,numpy,os

#===============================================================================
def structurerepresent(ch):
	if (ch=='H' or ch=='G' or ch=='I') :
		return 'H'
	elif ch=='E':
		return 'E'
	elif (ch=='b' or ch=='B' or ch=='T' or ch=='C'):
		return 'C'

def getsecstr(pdbid):
	command="~/Documents/proteins/stride/stride "+pdbid+".pdb > tempfile"
	os.system(command)
	with open("tempfile","r") as f1:
		lines=f1.read().splitlines()
	count=0
	for line in lines:
		count+=1
		if "-Phi-" in line:
			break
	lines=lines[count:]
	string=""
	for line in lines:
		secstr=line[24]
		rep = structurerepresent(secstr)
		string += rep
	return string
#=================================================================================

def getseq(pdbid):
	pdbFile = pdbid+".pdb"

	## First, open and parse the protein file
	p = PDBParser(PERMISSIVE=1)
	chainseq=""
	structure = p.get_structure(pdbFile, pdbFile)
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
			temp=(chainseq + '.')[:-1]
			excgstr=convert_exchange(temp)
	return chainseq,excgstr


#=====================================================================================
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
#============================================================================================
infile=sys.argv[1]
outfile=sys.argv[2]
with open(infile) as f1:
	pdblist=f1.read().splitlines()
for pdbid in pdblist:
	s1,s2=getseq(pdbid)
	s3=getsecstr(pdbid)
	print(pdbid)
	with open(outfile,"a") as f:
		f.write(pdbid+'\t'+s1+'\t'+s2+'\t'+s3+'\n')