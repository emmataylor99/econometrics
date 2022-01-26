# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:56:11 2022

@author: emmat
"""


### Part 1

# 1.11
import numpy as np

# define an arrays in numpy:
mat1 = np.array([[4, 9, 8],
                 [2, 6, 3]])
mat2 = np.array([[1, 5, 2],
                  [6, 6, 0],
                  [4, 8, 3]])

# use a numpy function:
result1 = np.exp(mat1)
print(f'result1: \n{result1}\n')

result2 = mat1 + mat2[[0,1]] # same as np.add(mat1, mat2[[0, 1]])

# use a method:
mat1_tr = mat1.transpose()
print(f'mat1_tr: \n{mat1_tr}\n')

# matrix algebra:
matprod = mat1.dot(mat2) # same as mat1 @ mat2
print(f'matprod: \n{matprod}\n')

# 1.12
import pandas as pd

# define a pandas DataFrame:
icecream_sales = np.array([30, 40, 35, 130, 120, 60])
weather_coded = np.array([0, 1, 0, 1, 1, 0])
customers = np.array([2000, 2100, 1500, 8000, 7200, 2000])
df = pd.DataFrame({'icecream_sales' : icecream_sales,
                   'weather_coded' : weather_coded,
                   'customers' : customers})

# define and assign an index (six ends of month starting in April, 2010)
# (details on generating indices are given in Chapter 10) :
ourIndex = pd.date_range(start='04/2010', freq='M', periods=6)
df.set_index(ourIndex, inplace=True)

# print the DataFrame
print(f'df: \n{df}\n')

# access columns by variable names:
subset1 = df[['icecream_sales', 'customers']]
print(f'subset1: \n{subset1}\n')

# access second to fourth row:
subset2 = df[1:4] # same as df['2010-05-31':'2010-07-31']
print(f'subset2: \n{subset2}\n')

# access rows and columbs by index and variable names:
subset3 = df.loc['2010-05-31', 'customers'] # same as df.loc[1,2]
print(f'subset3: \n{subset3}\n')

# access rows and columns by index and variable integer positions:
subset4 = df.iloc[1:4, 0:2]
# same as df.loc['2010-05-31':'2010-07-31', ['icecream_sales','weather']]
print(f'subset4: \n{subset4}\n')

# 1.13
# define a pandas DataFrame:
icecream_sales = np.array([30, 40, 35, 130, 120, 60])
weather_coded = np.array([0, 1, 0, 1, 1, 0])
customers = np.array([2000, 2100, 1500, 8000, 7200, 2000])
df = pd.DataFrame({'icecream_sales' : icecream_sales,
                   'weather_coded' : weather_coded,
                   'customers' : customers})

# define and assign an index (six ends of month starting in April, 2010)
# (details on generating indices are given in Chapter 10) :
ourIndex = pd.date_range(start='04/2010', freq='M', periods=6)
df.set_index(ourIndex, inplace=True)

# include sales two months ago:
df['icecream_sales_lag2'] = df['icecream_sales'].shift(2)
print(f'df: \n{df}\n')

# use a pandas.Categorical object to attach labels (0 = bad; 1 = good) :
df['weather'] = pd.Categorical.from_codes(codes=df['weather_coded'],
                                          categories=['bad', 'good'])
print(f'df: \n{df}\n')

# mean sales for each weather category:
group_means = df.groupby('weather').mean()
print(f'group_means: \n{group_means}\n')

# 1.14
import wooldridge as woo 

# load data: 
wage1 = woo.dataWoo('wage1')

# get type:
print(f'type(wage1): \n{type(wage1)}\n')

# get an overview:
print(f'wage1.head(): \n{wage1.head()}\n')

# 1.15
# import csv with pandas: 
df1 = pd.read_csv('etf5_m.csv', delimiter=',')
print(f'df1: \n{df1}\n')

# next portions of script do not apply to etf5_m.csv

# 1.17
import matplotlib.pyplot as plt

# create data:
x = [1, 3, 4, 7, 8, 9]
y = [0, 3, 6, 9, 7, 8]

# plot and save: 
plt.plot(x, y, color='black')
plt.savefig('PyGraphs/Graphs-Basics-a.pdf')
plt.close()

# 1.19
import scipy.stats as stats

# support of quadratic function
# (creates an array with 100 equispaced elements from -3 to 2):
x1 = np.linspace(-3, 2, num=100)
# function values for all these values:
y1 = x1 ** 2

# plot quadratic function: 
plt.plot(x1, y1, linestyle='-', color='black')
plt.savefig('PyGraphs/Graphs-Functions-a.pdf')
plt.close()

# same for normal density:
x2 = np.linspace(-4, 4, num=100)
y2 = stats.norm.pdf(x2)

# plot normal density:
plt.plot(x2, y2, linestyle='-', color='black')
plt.savefig('PyGraphs/Graphs-Functions-b.pdf')

# 1.20
# support for all normal densities:
x = np.linspace(-4, 4, num=100)
# get different density evaluations:
y1 = stats.norm.pdf(x, 0, 1)
y2 = stats.norm.pdf(x, 1, 0.5)
y3 = stats.norm.pdf(x, 0, 2)

# plot
plt.plot(x, y1, linestyle='-', color='black', label='standard normal')
plt.plot(x, y2, linestyle='--', color='0.3', label='mu = 1, sigma = 0.5')
plt.plot(x, y3, linestyle=':', color='0.6', label='$\mu = 0$, $\sigma = 2$')
plt.xlim(-3, 4)
plt.title('Normal Densities')
plt.ylabel('$\phi(x)$')
plt.xlabel('x')
plt.legend()
plt.savefig('PyGraphs/Graphs-BuildingBlocks.pdf')

# 1.21 
# support for all normal densities:
x = np.linspace(-4, 4, num=100)

# get different density evaluations:
y1 = stats.norm.pdf(x, 0, 1)
y2 = stats.norm.pdf(x, 0, 3)

# plot (a)
plt.figure(figsize=(4, 6))
plt.plot(x, y1, linestyle='-', color='black')
plt.plot(x, y2, linestyle='--', color='0.3')
plt.savefig('PyGraphs/Graphs-Export-a.pdf')
plt.close()

# plot (b)
plt.figure(figsize=(6, 4))
plt.plot(x, y1, linestyle='-', color='black')
plt.plot(x, y2, linestyle='--', color='0.3')
plt.savefig('PyGraphs/Graphs-Export-b.png')

# 1.22
affairs = woo.dataWoo('affairs')

# adjust codings to [0-4] (Categories require a start from 0):
affairs['ratemarr'] = affairs['ratemarr'] - 1

# use a pandas.Categorical object to attach labels for "haskids":
affairs['haskids'] = pd.Categorical.from_codes(affairs['kids'],
                                               categories=['no', 'yes'])
# ... and "marriage" (for example: 0 = 'very unhappy', 1 = 'unhappy',...):
mlab = ['very unhappy', 'unhappy', 'average', 'happy', 'very happy']
affairs['marriage'] = pd.Categorical.from_codes(affairs['ratemarr'],
                                                categories=mlab)

# frequency table in numpy (alphabetical order of elements):
ft_np = np.unique(affairs['marriage'], return_counts=True)
unique_elem_np = ft_np[0]
counts_np = ft_np[1]
print(f'unique_elem_np: \n{unique_elem_np}\n')
print(f'counts_up: \n{counts_np}\n')

# frequency table in pandas:
ft_pd = affairs['marriage'].value_counts()
print(f'ft_pd: \n{ft_pd}\n')

# frequency table with groupby:
ft_pd2 = affairs['marriage'].groupby(affairs['haskids']).value_counts()
print(f'ft_pd2: \n{ft_pd2}\n')

# contingency table in pandas:
ct_all_abs = pd.crosstab(affairs['marriage'], affairs['haskids'], margins=3)
print(f'ct_all_abs: \n{ct_all_abs}\n')
ct_all_rel = pd.crosstab(affairs['marriage'], affairs['haskids'], normalize='all')
print(f'ct_all_rel: \n{ct_all_rel}\n')

# share within "marraige" (i.e. within a row):
ct_row = pd.crosstab(affairs['marriage'], affairs['haskids'], normalize='index')
print(f'ct_row: \n{ct_row}\n')

# share within "haskids" (i.e. within a column):
ct_col = pd.crosstab(affairs['marriage'], affairs['haskids'], normalize='columns')
print(f'ct_col: \n{ct_col}\n')

# 1.23
affairs = woo.dataWoo('affairs')

# attach labels (see previous script):
affairs['ratemarr'] = affairs['ratemarr'] - 1
affairs['haskids'] = pd.Categorical.from_codes(affairs['kids'],
                                               categories=['no', 'yes'])
mlab = ['very unhappy', 'unhappy', 'average', 'happy', 'very happy']
affairs['marriage'] = pd.Categorical.from_codes(affairs['ratemarr'],
                                                categories=mlab)

# counts for all graphs:
counts = affairs['marriage'].value_counts()
counts_bykids = affairs['marriage'].groupby(affairs['haskids']).value_counts()
counts_yes = counts_bykids['yes']
counts_no = counts_bykids['no']

# pie chart (a):
grey_colors = ['0.3', '0.4', '0.5', '0.6', '0.7']
plt.pie(counts, labels=mlab, colors=grey_colors)
plt.savefig('PyGraphs/Descr-Pie.pdf')
plt.close()

# horizontal bar chart (b):
y_pos = [0, 1, 2, 3, 4] # the y locations for the bars
plt.barh(y_pos, counts, color='0.6')
plt.yticks(y_pos, mlab, rotation=60) # add and adjust labeling
plt.savefig('PyGraphs/Descr-Bar1pdf')
plt.close()

# stacked bar plot (c):
x_pos = [0, 1, 2, 3, 4] # the x locations for the bars
plt.bar(x_pos, counts_yes, width=0.4, color='0.6', label='Yes')
# with 'bottom=counts_yes' bars are added on top of previous ones:
plt.bar (x_pos, counts_no, width=0.4, bottom=counts_yes, color='0.3', label='No')
plt.ylabel('Counts')
plt.xticks(x_pos, mlab) # add labels on x axis
plt.legend()
plt.savefig('PyGraphs/Descr-Bar@.pdf')
plt.close()

# grouped bar plot (d)
# add left bars first and move bars to the left:
x_pos_leftbar = [-0.2, 0.8, 1.8, 2.8, 3.8]
plt.bar(x_pos_leftbar, counts_yes, width=0.4, color='0.6', label='Yes')
# add right bars first and move bars to the right:
x_pos_rightbar = [0.2, 1.2, 2.2, 3.2, 4.2]
plt.bar(x_pos_rightbar, counts_no, width=0.4, color='0.3', label='No')  
plt.ylabel('Counts')
plt.xticks(x_pos, mlab)
plt.legend()
plt.savefig('PyGraphs/Descr-Bar3.pdf')

# 1.24
ceosal1 = woo.dataWoo('ceosal1')

# extract roe:
roe = ceosal1['roe']

# subfigure a (histogram with counts):
plt.hist(roe, color='grey')
plt.ylabel('Counts')
plt.xlabel('roe')
plt.savefig('PyGraphs/Histogram1.pdf')
plt.close()

# subfigure b (histogram with density and explicit breaks):
breaks = [0, 5, 10, 20, 30, 60]
plt.hist(roe, color='grey', bins=breaks, density=True)
plt.ylabel('density')
plt.xlabel('roe')
plt.savefig('PyGraphs/Histogram2.pdf')


### Part 2
df2 = pd.read_csv('stockdata.csv', delimiter=',')

df2.head()

df2.tail()

### Part A Summary Statistics & Correlation Matrix

Data_summary = df2.describe()
print(f'Data_summary:\n{Data_summary}\n')

Corr_coef = df2.corr()
print(f'Corr_coef:\n{Corr_coef}\n')


### Part B Plotting

T = len(df2)
print(f'T: \n{T}\n')

df2.index = pd.date_range(start='2017-01', periods=T, freq='W')

trend = [i + 1 for i in range(0, len(df2))]
df2['trend'] = np.reshape(trend, (len(trend), 1))


# time series plot of adjusted closing prices:
plt.plot('TSLA', data=df2, color='black', linestyle='-')
plt.plot('JPM',data=df2, color='red', linestyle='-')
plt.plot('WFC',data=df2, color='orange', linestyle='-')
plt.plot('AMZN',data=df2,color='blue', linestyle='-')
plt.plot('NVDA',data=df2,color='green',linestyle='-')
plt.ylabel('Adj Close Price')
plt.xlabel('time')
plt.savefig('df2_plot.pdf')
plt.show()
plt.close()

# calculate return as the log difference:
df2[['ldTSLA','ldJPM','ldWFC','ldAMZN','ldNVDA']] = np.log(df2[['TSLA','JPM','WFC','AMZN','NVDA']]).diff(periods=1)

# calculate return as the difference:
df2[['dTSLA','dJPM','dWFC','dAMZN','dNVDA']] = df2[['TSLA','JPM','WFC','AMZN','NVDA']].diff(periods=1)

# time series plot of adjusted closing prices:
plt.plot('ldTSLA', data=df2, color='black', linestyle='-')
plt.plot('ldJPM',data=df2, color='red', linestyle='-')
plt.plot('ldWFC',data=df2, color='orange', linestyle='-')
plt.plot('ldAMZN',data=df2,color='blue', linestyle='-')
plt.plot('ldNVDA',data=df2,color='green',linestyle='-')
plt.ylabel('log Diff Adj Close Price')
plt.xlabel('time')
plt.savefig('df2_ldif_plot.pdf')
plt.show()
