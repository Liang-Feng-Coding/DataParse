import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
from sklearn.linear_model import LinearRegression
from numpy import shape
#from sklearn.model_selection import cross_val_predict
import csv
import pandas as pd


filename = "20200413column_chemistry-A1A2B1B2-LF.csv"

df = pd.read_csv(filename,engine="python",skipfooter=4,skiprows=(1,2,3,4,5))
df = df.dropna(axis=1,how="all",inplace=False)
isotope = df.iloc[:, 0]
#print(type(isotope))   #series
datafile = df.set_index('Unnamed: 0')
#print(datafile.iloc[:,1])
firstIn115 = datafile.loc['In115(LR)'].iat[0]


empty = pd.DataFrame()
#print(type(empty))  #dataframe

for i in range(datafile.shape[1]):
    #print(i)
    everyIn115 = datafile.loc['In115(LR)'].iat[i]
    coluInterCal = firstIn115/everyIn115*datafile.iloc[:,i]
    #print(type(coluInterCal))  #Series
    
    empty = empty.append(coluInterCal)
    #empty.to_csv('empty3.csv',header=False)
print(coluInterCal)
print(empty)
empty.to_csv('empty2.csv')

#print(datafile.shape[1])
#print(len(datafile))   #行数
#print(type(datafile))
#datafile.to_csv('20200413column-Sr.csv')






