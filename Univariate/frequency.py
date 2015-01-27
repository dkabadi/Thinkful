# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 13:13:09 2015

@author: darshankabadi
"""

import collections
import matplotlib.pyplot as plt
testlist = [1,4,5,6,9,9,9]
c=collections.Counter(testlist)
print c
count_sum=sum(c.values())

for k,v in c.iteritems():
    print "The frequency of number", k, "is", float(v)/count_sum

plt.hist(testlist)
plt.savefig('histogram')
plt.boxplot(testlist)
plt.savefig("boxplot")
plt.figure()
graph1 = stats.probplot(testlist, dist="norm", plot=plt)
plt.savefig("qqplot")