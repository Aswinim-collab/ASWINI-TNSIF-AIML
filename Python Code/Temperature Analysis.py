import numpy as np

# Temperature for 7 days
temperature = np.array([28, 31, 29, 33, 35, 30, 32])

# Average temperature
print("Average Temperature:", np.mean(temperature))

# Highest and lowest temperature
print("Highest Temperature:", np.max(temperature))
print("Lowest Temperature:", np.min(temperature))

# Days where temperature is above 30°C
days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday",
                 "Friday", "Saturday", "Sunday"])

print("Days above 30°C:")
print(days[temperature > 30])

# Increase all temperatures by 2°C
updated_temperature = temperature + 2

print("Updated Temperatures:", updated_temperature)
