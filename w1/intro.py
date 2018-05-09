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