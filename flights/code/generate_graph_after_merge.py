import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from airline_merge import merge
from edge_generator import edgeGenerator

df = pd.read_csv('../dataset/sample_delays_only_v3.csv')
airports = pd.read_csv('../dataset/airports.csv')

edge_list = edgeGenerator(df) 

chosen_airline = 'WN'

print(len(edge_list))
my_airline_airports, final_tab = merge(df, chosen_airline)
all_airports = list(airports['IATA_CODE'])

rest = list(set(all_airports).difference(set(my_airline_airports), set(final_tab)))
G = nx.Graph()
G.add_nodes_from(all_airports)
pos = nx.random_layout(G, seed=12)
nx.draw_networkx_nodes(G, pos, nodelist=rest, node_color='red')
nx.draw_networkx_nodes(G, pos, nodelist=my_airline_airports, node_color='green')
nx.draw_networkx_nodes(G, pos, nodelist=final_tab, node_color='orange')
nx.draw_networkx_edges(G, pos, edgelist=edge_list)
nx.draw_networkx_labels(G, pos)
plt.show()
