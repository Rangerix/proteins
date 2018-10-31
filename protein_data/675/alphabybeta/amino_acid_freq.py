#Protein Sequence Classification with Improved Extreme Learning Machine Algorithms

from collections import Counter
from Bio import SeqIO
import sys,numpy

#============================================================================================================
def getfreq (str):
	#alphabet=['a','c','d','e','f','g','h','i','k','l','m','n','p','q','r','s','t','v','w','y']
	eliminate=['b','j','o','u','x','z']
	alphabet="ACDEFGHIKLMNPQRSTVWY"
	freq=[ 0 for _ in range(26) ]
	for i in str:
		freq[ord(i)-ord('A')]+=1
	print(freq)
	return freq
#=============================================================================================================

outfile=sys.argv[2]
infile=sys.argv[1]
alphabet="ACDEFGHIKLMNPQRSTVWY"
with open(outfile,"a") as f:
	f.write("id"+'\t')
	for i in alphabet:
		f.write(i+'\t')
	f.write('\n')
with open(infile) as f1:
	fastalist=f1.read().splitlines()
for fastaid in fastalist:
	dict2=[0 for _ in range(26)]
	for seq_record in SeqIO.parse(fastaid+".fasta", "fasta"):
	    print(seq_record.id)
	    #print(seq_record.seq)
	    #print(len(seq_record))
	    dict1=getfreq(seq_record.seq)
	    dict2=numpy.add(dict2,dict1)
	    print("")
	print(dict2.tolist())
	alphabet="ACDEFGHIKLMNPQRSTVWY"
	indices=[]
	for i in alphabet:
		index=ord(i)-ord('A')
		indices.append(ord(i)-ord('A'))
	res=(dict2[indices])
	print(res)
	with open(outfile,"a") as f:
		f.write(fastaid+'\t')
		for i in res:
			f.write(str(i)+'\t')
		f.write('\n')
