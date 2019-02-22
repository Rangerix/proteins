import pandas as pd
import numpy as np
import sys
import regex as re
import collections

#==============================================================================
def aminofreq (str):
	#alphabet=['a','c','d','e','f','g','h','i','k','l','m','n','p','q','r','s','t','v','w','y']
	eliminate=['b','j','o','u','x','z']
	alphabet="ACDEFGHIKLMNPQRSTVWXY"
	indexes=[ord(i)-ord('A') for i in alphabet]
	freq=[ 0 for _ in range(26) ]
	for i in str:
		freq[ord(i)-ord('A')]+=1
	newfreq=[freq[x] for x in indexes]
	print(newfreq)
	return newfreq
#==============================================================================
def exc_sin_frq(str):
	alphabet="ABCDEF"
	freq=[ 0 for _ in range(len(alphabet)) ]
	for i in str:
		if i != "X":
			freq[ord(i)-ord('A')]+=1
	print(freq)
	return freq
#==============================================================================
def freq_seq(str):
	a=str.count('E')
	b=str.count('H')
	c=str.count('C')
	l=[a,b,c]
	return l
#==============================================================================
def excgfreq (tmpstr):
	#alphabet=['a','c','d','e','f','g','h','i','k','l','m','n','p','q','r','s','t','v','w','y']
	#alphabet=[ABCDEF]*[ABCDEF]
	alphabet=["AA","BA","CA","DA","EA","FA","AB","BB","CB","DB","EB","FB","AC","BC","CC","DC","EC","FC","AD","BD","CD","DD","ED"
	,"FD","AE","BE","CE","DE","EE","FE","AF","BF","CF","DF","EF","FF"]
	eliminate=['b','j','o','u','x','z']
	#alphabet="ACDEFGHIKLMNPQRSTVWY"
	freq={ i:0 for i in alphabet }
	for i in alphabet:
		freq[i]=(len(re.findall(i, tmpstr,overlapped=True)))

	#print(freq)
	#sortedfreq = collections.OrderedDict(sorted(freq.items()))
	return list(freq.values())
#==============================================================================

infile=sys.argv[1]
outfile=sys.argv[2]
df=pd.read_csv(infile)

for index,row in df.iterrows():
	pdbid=row['id']
	label=row['label']
	aseq=row['aseq']
	eseq=row['eseq']
	sseq=row['sseq']

	aminoacid="ACDEFGHIKLMNPQRSTVWXY"
	l1=aminofreq(aseq)
	exch_alpha="ABCDEF"
	l2=exc_sin_frq(eseq)

	l3=excgfreq(eseq)
	l4=freq_seq(sseq)
	
	joinchar="\t"
	s1=joinchar.join(map(str,l1))
	s2=joinchar.join(map(str,l2))
	s3=joinchar.join(map(str,l3))
	s4=joinchar.join(map(str,l4))

	with open(outfile,"a") as f:
		f.write(pdbid+joinchar+s1+joinchar+s2+joinchar+s3+joinchar+s4+joinchar+str(label)+'\n')
	print()