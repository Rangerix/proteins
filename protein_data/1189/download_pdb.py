#https://files.rcsb.org/download/1ETT.pdb
#usage: python3 download_pdb.py pdbfilelist
import urllib.request
import sys
#pdblstfile=input("Enter the list of pdbs : ")
pdblstfile=sys.argv[1]
print(pdblstfile)
with open(pdblstfile) as f:
	pdblist=f.read().splitlines()

for pdbid in pdblist:
	#print(pdbid)
	prefix="https://files.rcsb.org/download/"

	suffix=".pdb"
	url=prefix+pdbid+suffix
	print(url)

	filename=pdbid+suffix
	urllib.request.urlretrieve(url, filename)
