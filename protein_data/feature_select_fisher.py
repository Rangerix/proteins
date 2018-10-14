import pandas
import numpy
import sys
import scipy
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from skfeature.function.similarity_based import fisher_score

infile=sys.argv[1]
dataframe=pandas.read_csv(infile)

(a,b)= numpy.shape(dataframe)
print (a)
print (b)
#X = dataframe.values[:,0:b-1]
#y = dataframe.values[:,b-1]
X = dataframe.iloc[:,:-1]
y = dataframe.iloc[:,-1]
score = fisher_score.fisher_score(X, y)
ranking = fisher_score.feature_ranking(score)
colname=X.columns[ranking]
for i in colname:
	print(i,end=' ')
print()
'''
for loopval in range(5,b-1,5):
	X_new = SelectKBest(fisher_score, k=loopval).fit_transform(X, y)
	X_train, X_test, y_train, y_test = train_test_split(X_new, y,stratify=y ,test_size=0.1)


	clf=RandomForestClassifier()
	clf.fit(X_train,y_train)
	val=clf.score(X_test,y_test)
	print(loopval,val)
'''
for loopval in range(5,b-1,5):
	temp=ranking[0:loopval]
	#print(temp)
	X_new=X.iloc[:,temp]
	
	cross=20
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
