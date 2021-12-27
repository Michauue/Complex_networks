import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/sample_delays_only_v3.csv')
airports = pd.read_csv('../dataset/airports.csv')

edge_list=[]

for i in range(len(df)):
    if [df.iloc[i]['ORIGIN_AIRPORT'],df.iloc[i]['DESTINATION_AIRPORT']] not in edge_list and [df.iloc[i]['DESTINATION_AIRPORT'],df.iloc[i]['ORIGIN_AIRPORT']] not in edge_list:
        edge_list.append([df.iloc[i]['ORIGIN_AIRPORT'],df.iloc[i]['DESTINATION_AIRPORT']])
    if i % 10000 == 0:
        print(i)

print(len(edge_list))

G = nx.Graph()
G.add_nodes_from(airports['IATA_CODE'])
G.add_edges_from(edge_list)
nx.draw_kamada_kawai(G, with_labels=True)
plt.show()