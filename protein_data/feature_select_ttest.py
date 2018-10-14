import pandas
import numpy
import sys,math
import scipy
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier



#=================================================================================================
def myttest(X,y):
	#replace the chars in y by no : a:1 b:2 c:3 ...
	#y_new=[(ord(i)-96) for i in y]
	#y=y_new
	X=X.values
	y=y.values
	X=X.astype('float')
	y=y.astype('int')
	ClassSet = set(y)
	#print(ClassSet)
	(a,b)=numpy.shape(X)
	ttest_value=[]
	for i in range(0,b):
		ttest_i=[]
		sumVal=0
		fea=X[:,i]
		(N,)=numpy.shape(fea)
		#print(N)
		for c in ClassSet:
			temp1=fea[y[:]==c]
			xc=numpy.mean(temp1)
			temp1=temp1-xc
			temp2=numpy.sum(temp1**2)
			sumVal=sumVal+temp2
			C=len(ClassSet)
			Si2=sumVal/(N-C)
			Si=math.sqrt(Si2)
			
		for c in ClassSet:
			temp1=fea[y[:]==c]
			meanTotal=numpy.mean(fea)
			meanClass=numpy.mean(temp1)
			val=abs(meanTotal-meanClass)
			#N=fea.length()
			(nc,)=numpy.shape(temp1)
			Mc=math.sqrt(1/nc+a/N)
			if Mc*Si==0:
				#print(c,i,val,Mc,Si)
				val=-math.inf
			else:
				val=val/(Mc*Si)
			#print(c,i,val,Mc,Si)
			ttest_i.append(val)
		ttest_i_val=max(ttest_i)
		ttest_value.append(ttest_i_val)
	return ttest_value
#--------------------------------------------------------------------------------------------------
def feature_ranking(score):
	idx=numpy.argsort(score)
	return idx[::-1]
#==================================================================================================

infile=sys.argv[1]
dataframe=pandas.read_csv(infile)

(a,b)= numpy.shape(dataframe)
print (a)
print (b)
#X = dataframe.values[:,0:b-1]
#y = dataframe.values[:,b-1]
X = dataframe.iloc[:,:-1]
y = dataframe.iloc[:,-1]
score = myttest(X, y)
#for idx,val in enumerate(score):
#	print(idx,val)
ranking=feature_ranking(score)
#print(ranking)

colname=X.columns[ranking]
for i in colname:
	print(i,end=' ')
print()

for loopval in range(5,b-1,5):
	temp=ranking[0:loopval]
	#print(temp)
	X_new=X.iloc[:,temp]
	
	cross=10
	maxacc=0
	for _ in range(0,cross):
		test_size=(1/cross)
		X_train, X_test, y_train, y_test = train_test_split(X_new, y,stratify=y ,test_size=test_size)
		
		clf=RandomForestClassifier()
		clf.fit(X_train,y_train)
		val=clf.score(X_test,y_test)
		if val>maxacc:
			maxacc=val
			savetrainX=X_train
			savetrainY=y_train
			savetestX=X_test
			savetestY=y_test
	print(loopval,maxacc)
	#print(savetrainX,savetrainY)
	tmp=[savetrainX ,savetrainY]
	result=pandas.concat(tmp,axis=1)
	#print(result)
	outfile='train_'+str(loopval)+'_'+str(cross)+'.csv';
	#result.to_csv(outfile,index=False)
	#print(savetrainY)
	#print(savetestX)
	#print(savetestY)
	tmp=[savetestX ,savetestY]
	result=pandas.concat(tmp,axis=1)
	#print(result)
	outfile='test_'+str(loopval)+'_'+str(cross)+'.csv';
	#result.to_csv(outfile,index=False)
