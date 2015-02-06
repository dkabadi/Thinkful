# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 23:22:21 2015

@author: darshankabadi
"""

import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure()
test_data = np.random.normal(size=1000)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() #this will generate the first graph
plt.figure()
test_data2 = np.random.uniform(size=1000)   
 graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show() #this will generate the second graph