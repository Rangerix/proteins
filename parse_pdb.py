from Bio.PDB.PDBParser import PDBParser
from Bio import PDB                    
import warnings
from Bio import BiopythonWarning
warnings.simplefilter('ignore', BiopythonWarning)                                   
parser = PDBParser(PERMISSIVE=1)
structure_id = "1fat"
filename = "pdb1fat.ent"
structure = parser.get_structure(structure_id, filename)


model=structure[0]
chain=model["A"]
print(len(model.get_list()))


print(structure.get_full_id())
for chain in structure.get_chains():
	print(chain)
	i=0
	for temp in chain.get_residues():
		if PDB.is_aa(temp):
			i+=1
	print(i)			#length of each chain

