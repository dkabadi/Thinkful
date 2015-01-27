# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 22:57:36 2015

@author: darshankabadi
"""

import matplotlib.pyplot as plt
import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna()