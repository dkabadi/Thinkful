# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:42:39 2015

@author: darshankabadi
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
The Iris Dataset
=========================================================
This data sets consists of 3 different types of irises'
(Setosa, Versicolour, and Virginica) petal and sepal
length, stored in a 150x4 numpy.ndarray

The rows being the samples and the columns being:
Sepal Length, Sepal Width, Petal Length	and Petal Width.

The below plot uses the first two features.
See `here <http://en.wikipedia.org/wiki/Iris_flower_data_set>`_ for more
information on this dataset.
"""
print(__doc__)


# Code source: GaÃ«l Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets

# import some data to play with
iris = datasets.load_iris()
X = pd.DataFrame(iris.data[:, :2])  # we only take the first two features.
Y = pd.DataFrame(iris.target)
full=pd.concat([X,Y],1)
full.columns=['0','1','label']
dfTrain, dfTest = train_test_split(full, test_size=0.5)

def knn(x):
    clf = KNeighborsClassifier(n_neighbors=x)
    ##first paramter is the features you want to check, and the second paramter is the classification variable
    clf.fit(dfTrain[:,:2], dfTrain[:,2])
    check=np.random.randint(3,8,(1,2))
    ##this line predicts what the color will be of the test data set based off the features test[features] are basically your y variables
    preds = clf.predict(check)
    print "K=", x
    print "Label=", preds
