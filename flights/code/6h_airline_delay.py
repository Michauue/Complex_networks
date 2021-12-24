import pandas as pd
from colours import my_colours
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/sample_delays_only_v2.csv')
airlines = pd.read_csv('../dataset/airlines.csv')

hour_delay = df.loc[df['DEPARTURE_DELAY'] > 300].reset_index()
hour_delay = hour_delay.loc[hour_delay['ARRIVAL_DELAY'] > 300]
airline_to_delay = hour_delay.groupby(['AIRLINE']).count().sort_values('YEAR',ascending=True).reset_index()

print(airline_to_delay['AIRLINE'].values,airline_to_delay['index'].values)

length = np.arange(len(airline_to_delay['AIRLINE'].values))
plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor('dimgray')
plt.bar(length, airline_to_delay['index'].values, color=my_colours(len(airline_to_delay['AIRLINE'].values)))
plt.xticks(length, airline_to_delay['AIRLINE'].values)
# plt.savefig('temp_plot.png')
plt.show()

# hour_delay['CONNECTION'] = hour_delay['ORIGIN_AIRPORT']+hour_delay['DESTINATION_AIRPORT']

# print(hour_delay.loc[hour_delay['CONNECTION'] == '1129814831'])
# for i in range(len(hour_delay)):
#     if len(hour_delay.iloc[i]['CONNECTION']) > 6:
#         hour_delay = hour_delay.drop(index=i)
# print(hour_delay.loc[hour_delay['CONNECTION'] == '1129814831'])
# print(hour_delay)

# edge_list=[]

# for i in range(len(hour_delay['CONNECTION'])):
#     edge_list.append([hour_delay.iloc[i]['ORIGIN_AIRPORT'],hour_delay.iloc[i]['DESTINATION_AIRPORT']])

# print(edge_list)

# plt.savefig('hour_delay_airport.png')

# temp = hour_delay.groupby(['ORIGIN_AIRPORT']).count().sort_values('YEAR',ascending=False).head(10).reset_index()

# print(temp['ORIGIN_AIRPORT'].values,temp['DEPARTURE_DELAY'].values)
