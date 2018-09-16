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

'''
print("\nfor the chain : ",end='')
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
'''
#print all hetero residues of a chain
residues=chain.get_residues()
for res in residues:
	res_id=res.get_id()
	hetfield=res_id[0]
	if hetfield[0]=="H":
		print(res_id)


#print all coordinates od CA with B factor > 50
for model in structure.get_list():
	for chain in model.get_list():
		for residue in chain.get_list():
			if residue.has_id("CA"):
				ca=residue["CA"]
				if ca.get_bfactor()>50.0 :
					print(chain,residue.get_full_id()[3][1],ca.get_coord())