import pandas
import numpy
import sys
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

infile=sys.argv[1]
dataframe=pandas.read_csv(infile)

(a,b)= numpy.shape(dataframe)
print (a)
print (b)
X = dataframe.values[:,0:b-1]
y = dataframe.values[:,b-1]
X_train, X_test, y_train, y_test = train_test_split(X, y,stratify=y ,test_size=0.1)


clf=RandomForestClassifier()
clf.fit(X_train,y_train)
val=clf.score(X_test,y_test)
print(val)