import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/sample_delays_only_v2.csv')
airlines = pd.read_csv('../dataset/airlines.csv')

hour_delay = df.loc[df['DEPARTURE_DELAY'] > 60].reset_index()
hour_delay = hour_delay.loc[hour_delay['ARRIVAL_DELAY'] > 60]
airline_to_delay = hour_delay.groupby(['AIRLINE']).count().sort_values('YEAR',ascending='False')

hour_delay['CONNECTION'] = hour_delay['ORIGIN_AIRPORT']+hour_delay['DESTINATION_AIRPORT']

print(hour_delay)

edge_list=[]

for i in range(len(hour_delay['CONNECTION'])):
    edge_list.append([hour_delay.iloc[i]['CONNECTION'][:3],hour_delay.iloc[i]['CONNECTION'][3:]])

# print(edge_list)
G = nx.Graph()
G.add_nodes_from(hour_delay['ORIGIN_AIRPORT'])
G.add_edges_from(edge_list)

nx.draw(G, with_labels=True)
# plt.savefig('hour_delay_airport.png')

temp = hour_delay.groupby(['ORIGIN_AIRPORT']).count().sort_values('YEAR',ascending=False).head(10).reset_index()

print(temp['ORIGIN_AIRPORT'].values,temp['DEPARTURE_DELAY'].values)

print(airlines)