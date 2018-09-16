4.835975863
import sys
infilename =sys.argv[1]
with open(infilename) as myfile:
	pdbidlist=myfile.read().splitlines()
for x in pdbidlist:
	v=x.split()
	#v[0] = volume
	val=float(v[0])
	val=val**(2/3)
	#v[1] = surface area
	val/=float(v[1])
	val*=4.835975863
	print(v[2],val)