"""
Ahriel Godoy
871928876
The data was downloaded from https://www.ncdc.noaa.gov/
"""

import numpy as np
import pandas as pd

# These are the mean temperatures of the ten cities for every hour of the day for the entire year of 2014

# Read values for the various cities
aurora = pd.read_csv('aurora.csv')
bakersfield = pd.read_csv('bakersfield.csv')
boston = pd.read_csv('boston.csv')
bristol = pd.read_csv('bristol.csv')
chicago = pd.read_csv('chicago.csv')
cosprings = pd.read_csv('cosprings.csv')
houston = pd.read_csv('houston.csv')
miami = pd.read_csv('miami.csv')
newyork = pd.read_csv('newyork.csv')
valdez = pd.read_csv('valdez.csv')

# Add the temperature column into one array
city_temps = pd.DataFrame(aurora[['HLY.TEMP.NORMAL']])
city_temps.columns = ['Aurora, CO']
city_temps['Bakersfield, CA'] = bakersfield[['HLY.TEMP.NORMAL']]
city_temps['Boston, MA'] = boston[['HLY.TEMP.NORMAL']]
city_temps['Tri-Cities, TN'] = bristol[['HLY.TEMP.NORMAL']]
city_temps['Chicago, IL'] = chicago[['HLY.TEMP.NORMAL']]
city_temps['COSPRINGS, CO'] = cosprings[['HLY.TEMP.NORMAL']]
city_temps['Houston, TX'] = houston[['HLY.TEMP.NORMAL']]
city_temps['Miami, FL'] = miami[['HLY.TEMP.NORMAL']]
city_temps['New York, NY'] = newyork[['HLY.TEMP.NORMAL']]
city_temps['Valdez, AK'] = valdez[['HLY.TEMP.NORMAL']]

# city_temps.index = valdez[['DATE']]

# There are only 24x365 hours per year, so we have missing data points
# Calculate the missing data points and give them a value of 0
missing_rows = (10000 - len(valdez[['DATE']]))

# This is the 10 x 1241 matrix
zeros_array = np.empty( (missing_rows, 10) )
zeros_array[:] = np.nan
empty_df = pd.DataFrame(zeros_array, columns=[
    'Aurora, CO', 'Bakersfield, CA', 'Boston, MA', 'Tri-Cities, TN', 'Chicago, IL', 'COSPRINGS, CO', 'Houston, TX',
    'Miami, FL', 'New York, NY', 'Valdez, AK'])

# This is the 10 x 10000 matrix in dataframe form
temperatures = city_temps.append(empty_df, ignore_index=True)


# Since there are only 8759 values, I entered NaN for the difference up to 10000
temperatures.to_csv('temperatures.csv', index = False)