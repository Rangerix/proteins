#Protein Sequence Classification with Improved Extreme Learning Machine Algorithms

from collections import Counter
from Bio import SeqIO
import sys,numpy
import regex as re
#============================================================================================================
def getfreq_am (str):
	#alphabet=['a','c','d','e','f','g','h','i','k','l','m','n','p','q','r','s','t','v','w','y']
	eliminate=['b','j','o','u','x','z']
	alphabet="ACDEFGHIKLMNPQRSTVWY"
	freq=[ 0 for _ in range(26) ]
	for i in str:
		freq[ord(i)-ord('A')]+=1
	print(freq)
	return freq
#=============================================================================================================

def getfreq_ex (tmpstr):
	#alphabet=['a','c','d','e','f','g','h','i','k','l','m','n','p','q','r','s','t','v','w','y']
	#alphabet=[ABCDEF]*[ABCDEF]
	tmpstr=convert_exchange(tmpstr)
	alphabet=["AA","BA","CA","DA","EA","FA","AB","BB","CB","DB","EB","FB","AC","BC","CC","DC","EC","FC","AD","BD","CD","DD","ED"
	,"FD","AE","BE","CE","DE","EE","FE","AF","BF","CF","DF","EF","FF"]
	eliminate=['b','j','o','u','x','z']
	freq={ i:0 for i in alphabet }
	for i in alphabet:
		freq[i]=(len(re.findall(i, tmpstr,overlapped=True)))

	#print(freq)
	#sortedfreq = collections.OrderedDict(sorted(freq.items()))
	return freq
#=============================================================================================================
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
alphabet1="ACDEFGHIKLMNPQRSTVWY"
alphabet2=["AA","BA","CA","DA","EA","FA","AB","BB","CB","DB","EB","FB","AC","BC","CC","DC","EC","FC","AD","BD","CD","DD","ED"
	,"FD","AE","BE","CE","DE","EE","FE","AF","BF","CF","DF","EF","FF"]

with open(outfile,"a") as f:
	for i in alphabet1:
		f.write(i+'\t')
	for i in alphabet2:
		f.write(i+'\t')
	f.write('\n')

with open(infile) as f1:
	sequences=f1.read().splitlines()

for line in sequences:
	dict1=[0 for _ in range(26)]
	dict1=getfreq_am(line)
	dict2=getfreq_ex(line)
	#print(dict2.tolist())
	#print the details of dict1 (this is an array)--------------
	indices=[]
	for i in alphabet1:
		index=ord(i)-ord('A')
		indices.append(ord(i)-ord('A'))
	dict1=numpy.array(dict1)
	res=(dict1[indices])
	print(res)
	with open(outfile,"a") as f:
		for i in res:
			f.write(str(i)+'\t')
	#print the details if dict2 ( dictionary )------------------
	res=[]
	for i in alphabet2:
		print(i,dict2[i],end='\t')
		res.append(dict2[i])
	print()
	#resarr=numpy.array(res)
	with open(outfile,"a") as f:
		for i in res:
			f.write(str(i)+'\t')
		f.write('\n')
