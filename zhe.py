
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the Excel file
file_path = '最终数据.xlsx'  # Replace with the actual file path
df = pd.read_excel(file_path)

# Customize x-axis range
start_x = 0  # Replace with your desired start value
end_x = 6500  # Replace with your desired end value
custom_x_points = list(range(start_x, end_x + 1))

# Make sure the number of rows in the DataFrame matches the custom x-axis points
if len(df) != len(custom_x_points):
    print("Warning: The number of rows in the DataFrame does not match the custom x-axis points.")
    print("Adjusting the DataFrame to match the custom x-axis points.")
    df = df.iloc[:len(custom_x_points)]

# Plot Temperature
plt.figure(figsize=(8, 6))
plt.plot(custom_x_points, df['Temperature'], label='Temperature', linestyle='-', color='blue', linewidth=0.5)
plt.axhline(y=18, color='r', linestyle='--', label='Temperature Upper Limit (25°C)')
plt.axhline(y=22, color='b', linestyle='--', label='Temperature Lower Limit (21°C)')
plt.ylim(0, 80)
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.title('Temperature')
plt.show()

# Plot Humidity
plt.figure(figsize=(8, 6))
plt.plot(custom_x_points, df['Humidity'], label='Humidity', linestyle='-', color='blue', linewidth=0.5)
plt.axhline(y=61, color='g', linestyle='--', label='Humidity Lower Limit (46%)')
plt.axhline(y=69, color='m', linestyle='--', label='Humidity Upper Limit (54%)')
plt.ylim(0, 80)
plt.xlabel('Time')
plt.ylabel('Humidity (%)')
plt.legend()
plt.title('Humidity')
plt.show()

# Plot Radar1
plt.figure(figsize=(8, 6))
plt.plot(custom_x_points, df['radar1'], label='Radar1', linestyle='-', color='blue', linewidth=0.5)
plt.ylim(0, 2)
plt.xlabel('Time')
plt.ylabel('Radar1')
plt.legend()
plt.title('Fabric operator behavior')
plt.show()

# Plot Radar2
plt.figure(figsize=(8, 6))
plt.plot(custom_x_points, df['radar2'], label='Radar2', linestyle='-', color='blue', linewidth=0.5)
plt.ylim(0, 2)
plt.xlabel('Time')
plt.ylabel('Radar2')
plt.legend()
plt.title('Equipment operator behavior')
plt.show()

# Plot Voltage
plt.figure(figsize=(8, 6))
plt.plot(custom_x_points, df['Voltage'], label='Voltage', linestyle='-', color='blue', linewidth=0.3)
plt.axhline(y=220, color='orange', linestyle='--', label='Voltage Limit (220)')
plt.ylim(200, 250)
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.legend()
plt.title('Voltage')
plt.show()

# Plot Current
plt.figure(figsize=(8, 6))
plt.plot(custom_x_points, df['current'], label='Current', linestyle='-', color='blue', linewidth=0.3)
plt.ylim(0, 2)
plt.xlabel('Time')
plt.ylabel('Current')
plt.legend()
plt.title('Current')
plt.show()

# Plot Power
plt.figure(figsize=(8, 6))
plt.plot(custom_x_points, df['power'], label='Power', linestyle='-', color='blue', linewidth=0.3)
plt.ylim(0, 450)
plt.xlabel('Time')
plt.ylabel('Power')
plt.legend()
plt.title('Power')
plt.show()