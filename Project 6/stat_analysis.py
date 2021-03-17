"""
Ahriel Godoy
871928876
"""

import statistics
import pandas as pd
import sys


def stats(city, array):
    mean = statistics.mean(array)
    st_dev = statistics.stdev(array)
    mode = statistics.mode(array)
    median = statistics.median(array)

    print(f"{city} had the following statistics in 2014: ")
    print(f"Mean               : {round(mean, 1)} F")
    print(f"Standard Deviation : {round(st_dev, 1)} F")
    print(f"Mode               : {mode} F")
    print(f"Median             : {median} F")
    print()
    return


# Redirect stdout into the file "output.txt", anything that would be printed in console is written to the file instead
sys.stdout = open('output.txt', 'wt')

# Read the file already created with pandas and create a dataframe
temperatures = pd.read_csv('temperatures.csv')

# Drop the rows that have missing data, NaN
temperatures = temperatures.dropna()

# Convert the dataframe into a numpy array
my_array = temperatures.to_numpy()

# Create a list of column headers
city_names = list(temperatures.columns.values)

for i, city in enumerate(city_names):
    temp_column = [row[i] for row in my_array]
    stats(city, temp_column)

# Print column names used in the file
print()
print(city_names)
print()

# Print 3 rows of the dataframe as sample data
print(temperatures.head(3))
