#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filename = '2026-10.csv'
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

#dataframe["DATE"] = pd.to_datetime(dataframe['DATE'], format="%Y-%m-%d")

#fig, ax = plt.subplots()
#ax.plot(dataframe["DATE"], dataframe["MINUTES"])
#ax.plot(dataframe["DATE"], dataframe["TMIN"])
#fig.autofmt_xdate()
#fig.show()

# generate graph from tally CSV

# total number of outages
# duration of outages (uptime %)
# longest continuous block
# average time between outages
