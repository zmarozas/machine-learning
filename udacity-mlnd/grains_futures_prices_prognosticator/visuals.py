###########################################
# Suppress matplotlib user warnings
# Necessary for newer version of matplotlib
import warnings
warnings.filterwarnings("ignore", category = UserWarning, module = "matplotlib")
#
# Display inline matplotlib plots with IPython
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
###########################################

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import numpy as np

def plot_numerical_series(data):
	'''
	The code below 
	plots each series as a separate subplot.
	'''

	values = data.values
	# specify columns to plot
	groups = [0, 1, 2, 3,4 ]
	i = 1
	# plot each column
	plt.figure()
	for group in groups:
		plt.subplot(len(groups), 1, i)
		plt.plot(values[:, group])
		plt.title(data.columns[group], y=0.5, loc='right')
		i += 1
	plt.show()