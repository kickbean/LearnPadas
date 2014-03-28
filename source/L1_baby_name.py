'''
baby name

Created on Mar 27, 2014

@author: Songfan
'''
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

print 'Pandas version ' + pd.__version__

''' Create Data '''
# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

# Use zip to merge two list
BabyDataSet = zip(names,births)
print BabyDataSet

# DataFrame for holding contents similar to sql table
df = pd.DataFrame(data=BabyDataSet, columns=['Names','Births'])
print df

# Export DataFrame to csv file
df.to_csv('births1880.csv', index=False, header=False)

''' Get Data '''
LOCATION = './births1880.csv'
df = pd.read_csv(LOCATION, header=None)    # pandas treats the first row as head by default
print df
df = pd.read_csv(LOCATION, names=['Names','Births'])
print df

# Delete csv file when done using
os.remove(LOCATION)


''' Prepare Data '''
# Check data type
print df.dtypes
print df.Births.dtypes


''' Analyze Data '''
# Find max by sorting
birth_sorted = df.sort(['Births'], ascending=[0])
print birth_sorted.head(1)

# By direct call of max
print df['Births'].max()


''' Present Data '''
print 'present data ... '
# Create graph
df['Births'].plot()

# Max value in the data set
max_val = df['Births'].max()

# Name associated with max val
# similar to select name from df where Births=max_val
max_name = df['Names'][df['Births']==max_val].values
print max_name

# Text to display on graph
text = str(max_val) + '-' + max_name

# Add text to graph
plt.annotate(text, xy=(1,max_val), xytext=(8,0), 
             xycoords=('axes fraction','data'), textcoords='offset points')

print 'The most popular name'
print df[df['Births'] == df['Births'].max()]



#plt.imshow(np.random.rand(4,4))
plt.show()

