'''
Created on Mar 27, 2014

@author: Songfan
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set seed
np.random.seed(111)
def create_dataset(Number=1):
    output = []
    for i in range(Number):
        # create a weekly (mondays) date range
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')
        
        # create random data
        data = np.random.randint(low=25,high=1000,size=len(rng))
        
        # Status and State pool
        status = [1,2,3]
        state = ['GA','FL','fl','NY','NJ','TX']
        
        # Make a random list of status and state
        random_status = [status[np.random.randint(low=0,high=len(status))] for i in range(len(rng))]
        random_state = [state[np.random.randint(low=0,high=len(state))] for i in range(len(rng))]
        
        output.extend(zip(random_state, random_status, data, rng))
    return output
        
        
dataset = create_dataset(4)
df = pd.DataFrame(data=dataset, columns=['State','Status','CustomerCount','StatusDate'])
print df.info()
print df.head(5)        
print df.index
        
        