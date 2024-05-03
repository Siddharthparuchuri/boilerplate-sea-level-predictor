import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data from epa-sea-level.csv
df = pd.read_csv('epa-sea-level.csv')

# Create a scatter plot of the data
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Get the slope and y-intercept of the line of best fit for the entire dataset
slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Plot the line of best fit for the entire dataset
years = range(1880, 2051)
plt.plot(years, [slope * year + intercept for year in years], 'r', label='Entire dataset')

# Get the slope and y-intercept of the line of best fit for the data since 2000
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

# Plot the line of best fit for the data since 2000
plt.plot(years, [slope_recent * year + intercept_recent for year in years], 'g', label='Since 2000')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Add legend
plt.legend()

# Save and return the image
plt.savefig('sea_level_rise.png')
plt.show()
