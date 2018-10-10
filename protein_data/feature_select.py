import pandas
import numpy
import sys
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif

infile=sys.argv[1]
dataframe=pandas.read_csv(infile)

(a,b)= numpy.shape(dataframe)
print (a)
print (b)
X = dataframe.values[:,0:b-1]
y = dataframe.values[:,b-1]

for loopval in range(5,b-1,5):
	X_new = SelectKBest(mutual_info_classif, k=loopval).fit_transform(X, y)
	X_train, X_test, y_train, y_test = train_test_split(X_new, y,stratify=y ,test_size=0.1)


	clf=RandomForestClassifier()
	clf.fit(X_train,y_train)
	val=clf.score(X_test,y_test)
	print(loopval,val)
