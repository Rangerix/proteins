from Bio.PDB.PDBParser import PDBParser
from Bio import PDB                    
import warnings
from Bio import BiopythonWarning
warnings.simplefilter('ignore', BiopythonWarning)                                   
parser = PDBParser(PERMISSIVE=1)
structure_id = "1fat"
filename = "1fat.pdb"
structure = parser.get_structure(structure_id, filename)


model=structure[0]
chain=model["A"]
print(len(model.get_list()))


print(structure.get_full_id())
for chain in structure.get_chains():
	i=0
	for temp in chain.get_residues():
		if PDB.is_aa(temp):
			i+=1
	print(chain," length : ",i)			#length of each chain


print("for the chain : ",end='')
print(chain)
residues=chain.get_residues()	#print all residues of a chain
for res in residues:
	print("residue name : ",end='')
	print(res.get_resname(),end='')
	if PDB.is_aa(res):
		print(" amino acid")
	else:
		print(" not amino acid")
	print("atoms and their coordinates in the residue : ")
	atoms=res.get_atom()
	for atom in atoms:
		print(atom.get_name(),end=' ')
		print(atom.get_coord())
	print('')
     

