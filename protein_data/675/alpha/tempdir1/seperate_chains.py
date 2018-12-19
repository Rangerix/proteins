import os,sys
infilename =sys.argv[1]
with open(infilename) as myfile:
	pdbidlist=myfile.read().splitlines()
for pdbid in pdbidlist:
	pdbfile=pdbid+".pdb"
	command="grep ^ATOM "+pdbfile+" > tempfile"
	os.system(command)
	#now we have to seperate the chains
	#chain id can be A-Z,a-z,0-9
	with open("tempfile") as myfile:
		wholefile=myfile.read().splitlines()
	print(pdbfile)
	for eachline in wholefile:
		foundchainid=eachline[21]
		#print(foundchainid,end=',')
		subfilename=pdbid+foundchainid+".pdb"
		with open(subfilename,"a") as myfile:
			myfile.write(eachline)
			myfile.write("\n")