# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pickle

x = np.array([1, -1, 2, -2, 3])

plt.plot(x)
plt.show()


print(3/5)

# create dictionary containing all your data
data = {'stim': np.array([1, 2, 3]), 'response': np.array([6, 2, 0])}

# save data in pickle format
with open('my_data.pickle', 'wb') as f:
    pickle.dump(data, f)

# open data from file
with open('my_data.pickle', 'rb') as f:
    new_data_variable = pickle.load(f)

# now new_data_variable is equal to the dict:
# {'stim': np.array([1, 2, 3]), 'response': np.array([6, 2, 0])}
print(new_data_variable)

#%%
import numpy as np
A = np.matrix
#%%
# imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read data into a DataFrame
data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
data.head()

# print the shape of the DataFrame
data.shape

# visualize the relationship between the features and the response using scatterplots
fig, axs = plt.subplots(1, 3, sharey=True)
data.plot(kind='scatter', x='TV', y='sales', ax=axs[0], figsize=(16, 8))
data.plot(kind='scatter', x='radio', y='sales', ax=axs[1])
data.plot(kind='scatter', x='newspaper', y='sales', ax=axs[2])

# this is the standard import if you're using "formula notation" (similar to R)
import statsmodels.formula.api as smf

# create a fitted model in one line
lm = smf.ols(formula='sales ~ TV', data=data).fit()

# print the coefficients
lm.params

# manually calculate the prediction
7.032594 + 0.047537*50

# you have to create a DataFrame since the Statsmodels formula interface expects it
X_new = pd.DataFrame({'TV': [50]})
X_new.head()
# use the model to make predictions on a new value
lm.predict(X_new)

# create a DataFrame with the minimum and maximum values of TV
X_new = pd.DataFrame({'TV': [data.TV.min(), data.TV.max()]})
X_new.head()

# make predictions for those x values and store them
preds = lm.predict(X_new)
preds
#test = np.array(preds)
#test

# first, plot the observed data
data.plot(kind='scatter', x='TV', y='sales')

# then, plot the least squares line
plt.plot(X_new, preds, c='red', linewidth=2)

# print the confidence intervals for the model coefficients
lm.conf_int()

# print the p-values for the model coefficients
lm.pvalues

