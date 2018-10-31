#downloads fasta file, given ID as command line argument
#https://www.rcsb.org/pdb/download/downloadFastaFiles.do?structureIdList=1FAT&compressionType=uncompressed
import urllib.request
import sys
#pdblstfile=input("Enter the list of pdbs : ")
pdblstfile=sys.argv[1]
print(pdblstfile)
with open(pdblstfile) as f:
	pdblist=f.read().splitlines()

for pdbid in pdblist:
	#print(pdbid)
	prefix="https://www.rcsb.org/pdb/download/downloadFastaFiles.do?structureIdList="
	pdbid=pdbid.strip()
	suffix="&compressionType=uncompressed"
	url=prefix+pdbid.strip()+suffix
	print(url)

	filename=""+pdbid+".fasta"
	urllib.request.urlretrieve(url, filename)
