import glob
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.signal import argrelextrema
import numpy as np
  
# specifying the path to csv files
path = os.getcwd()
  
# csv files in the path
files = glob.glob(path + "/data/*.csv")
  
# defining an empty list to store 
# content
data_frame = pd.DataFrame()
content = []
  
# checking all the csv files in the 
# specified path
for filename in files:
    
    # reading content of csv file
    # content.append(filename)
    df = pd.read_csv(filename, index_col=None)
    content.append(df)
  
# converting content to data frame
data_frame = pd.concat(content)

data_frame['Date'] = pd.to_datetime(data_frame['Date'])

data_frame['Cap'] = pd.to_numeric(data_frame['Vol'], errors = 'coerce')

cap = data_frame.groupby(['Date'])['Cap'].sum()

cap.plot.line(x = cap.index, y = cap)

cap = pd.DataFrame(cap)

n = 25

cap['min'] = cap.iloc[argrelextrema(np.array(cap.Cap), 
                                    np.less_equal, 
                                    order = n)[0]]['Cap']

cap['max'] = cap.iloc[argrelextrema(np.array(cap.Cap), 
                                    np.greater_equal, 
                                    order = n)[0]]['Cap']

plt.scatter(cap.index, cap['min'], c='r')
plt.scatter(cap.index, cap['max'], c='g')
plt.plot(cap.index, cap['Cap'], c = 'black')
plt.show()

cap.to_csv('market_cap.csv')