#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys
import os

if len(sys.argv) > 1:
  first_param = sys.argv[1]
else:
  print("No arguments provided.")
  sys.exit(1)

if os.path.isfile(first_param):
  filename = first_param
else:
  print("Invalid file.")
  sys.exit(1)

print(f"Reading file: {filename}")
df = pd.read_csv(filename)

# Convert to datetime and set as index
df['DATE'] = pd.to_datetime(df['DATE'])
df.set_index('DATE', inplace=True)

df['DAYS'] = df['DAYS'] / 24 /60

ax = df.plot.area(title="Uptime (WAN)", legend=False, rot=75)
#ax.margins(0)

# Set x-axis ticks to appear once per day (every day)
# To show only the 1st of each month, use: mdates.DayLocator(bymonthday=[1])
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))

# Format the labels (e.g., "Jan 01")
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.show()
