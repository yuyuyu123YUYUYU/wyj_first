import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read data from Excel file
excel_file_path = '5.xlsx'
df = pd.read_excel(excel_file_path, sheet_name='Sheet1')  # Update 'Sheet1' to the actual sheet name

# Extract the 'Power' column from the DataFrame and convert to NumPy array
power_values = np.array(df['Power'])

# Generate x-axis values
x_values = np.arange(len(power_values))

# Set threshold values for shading
lower_threshold = 100
upper_threshold = 150

# Create a boolean array for shading
shading_condition = (power_values >= lower_threshold) & (power_values <= upper_threshold)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the power values
ax.plot(x_values, power_values, label='Power')

# Shade the regions between lower and upper thresholds
#ax.fill_between(x_values, lower_threshold, upper_threshold, where=shading_condition, color='lightgray', alpha=0.5, label='Threshold Range')

# Add shaded regions from data point 0 to 146
ax.axvspan(0, 293, color='purple', alpha=0.2, label='Stretch phase')
ax.axvspan(293, 329, color='green', alpha=0.2, label='Reset phase')
ax.axvspan(329, 249, color='blue', alpha=0.2, label='Transformation stage')

# Set x-axis limits to remove empty space on the left and right
ax.set_xlim(0, len(power_values) - 1)

# Hide x-axis tick labels
ax.set_xticks([])

# Customize the plot
ax.set_xlabel('')
ax.set_ylabel('Power')
ax.set_title('The first set of sample 1 experimental procedure')
ax.legend()

# Show the plot
plt.show()
