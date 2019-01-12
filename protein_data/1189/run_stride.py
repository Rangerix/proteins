import sys,os


#===========================================================
def structurerepresent(ch):
	if (ch=='H' or ch=='G' or ch=='I') :
		return 'H'
	elif ch=='E':
		return 'E'
	elif (ch=='b' or ch=='B' or ch=='T' or ch=='C'):
		return 'C'
#===========================================================

infile=sys.argv[1]
with open(infile,"r") as f:
	pdblist=f.read().splitlines()
for pdbid in pdblist:
	print(pdbid)
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
	#print(string)
	newfilename=pdbid+".secstr"
	with open(newfilename,"w") as f1:
		f1.write(string)