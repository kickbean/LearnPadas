'''
Created on Mar 27, 2014

@author: Songfan
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

''' Create Data '''
# The inital set of baby names
names = ['Bob','Jessica','Mary','John','Mel']

# Generate 1000 random names
np.random.seed(500)
random_names = [names[np.random.randint(low=0, high=len(names))] for i in range(1000)]
#print random_names[:10]

births = [np.random.randint(low=0,high=1000) for i in range(1000)]
#print births[:10]

BabyDataSet = zip(random_names, births)
#print BabyDataSet[:10]

df = pd.DataFrame(data=BabyDataSet, columns=['Names','Births'])
#print df[:10]

''' Prepare Data '''
#print df.info()
#print df.head(6)    # get the first 6 items
#print df.tail()     # get the last n items

print df['Names'].unique()

print df['Names'].describe()

# Cumulate 
name = df.groupby('Names')
print name.sum()

''' Analyze Data '''



''' Present Data '''
name.plot(kind='bar')
plt.show()