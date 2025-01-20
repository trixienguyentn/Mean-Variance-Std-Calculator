import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# import data
data = pd.read_csv('epa-sea-level.csv')

#-------------------------------------------------------------------------------------------
# create a scatter plot
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.5)
slope1, intercept1, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
x1 = pd.Series(range(data['Year'].min(), 2051))
y1 = slope1 * x1 + intercept1
plt.plot(x1, y1, 'r', label='Fit: All Data')
plt.savefig('scatter_plot.png')
plt.show()

#-------------------------------------------------------------------------------------------
# Line of best fit from year 2000
recent_data = data[data['Year'] >= 2000]
slope2, intercept2, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
x2 = pd.Series(range(2000, 2051))
y2 = slope2 * x2 + intercept2
plt.plot(x2, y2, 'g', label='Fit: 2000-Present')

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.grid(True)

plt.savefig('sea_level_plot.png')
plt.show()
