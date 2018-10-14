from collections import Counter
from Bio import SeqIO
import sys,numpy
import regex as re
import collections


def getfreq (tmpstr):
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
	return freq
#------------------------------------------------------------------------------------


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
alphabet=["AA","BA","CA","DA","EA","FA","AB","BB","CB","DB","EB","FB","AC","BC","CC","DC","EC","FC","AD","BD","CD","DD","ED"
	,"FD","AE","BE","CE","DE","EE","FE","AF","BF","CF","DF","EF","FF"]
with open(outfile,"a") as f:
	f.write("id"+' ')
	for i in alphabet:
		f.write(i+' ')
	f.write('\n')

with open(infile) as f1:
	fastalist=f1.read().splitlines()

for fastaid in fastalist:
	dict2={ i:0 for i in alphabet }
	#dict2=collections.OrderedDict(sorted(dict2.items()))
	for seq_record in SeqIO.parse(fastaid+".fasta", "fasta"):
	    print(seq_record.id)
	    #print(seq_record.seq)
	    #print(len(seq_record))
	    tmpstr1=str(seq_record.seq)
	    tmpstr=convert_exchange(tmpstr1)
	    
	    dict1=getfreq(tmpstr)
	    print(dict1)
	    dict2=Counter(dict1)+Counter(dict2)
	    '''
	    dict2=numpy.add(dict2,dict1)
	    print("")
	    '''


	#print(dict2)
	res=[]
	for i in alphabet:
		print(i,dict2[i],end='\t')
		res.append(dict2[i])
	print()
	resarr=numpy.array(res)
	with open(outfile,"a") as f:
		f.write(fastaid+' ')
		numpy.savetxt(f,resarr.reshape(1,resarr.shape[0]),fmt="%d",delimiter=' ')
