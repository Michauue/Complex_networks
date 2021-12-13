import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math as m

from numpy.lib.shape_base import _hvdsplit_dispatcher

filename = 'relacje.txt'
lines = [line.split(':') for line in open(filename, 'r')]
connections_list = []
for line in lines:
    key = line[0].strip()
    for element in line[1].split(','):
        connections_list.append((key, element.strip()))


G = nx.Graph()
G.nodes(data=True)
G.add_edges_from(connections_list)
nx.draw_spring(G, with_labels=True)
# plt.show()
# plt.savefig('tempgraph.png')
# print('Rząd:', G.number_of_nodes())
# print('Rozmiar:', G.size())
# print('Stopień wierzchołków:', nx.degree(G))
# print('Gęstość:', nx.density(G))
# print('Bliskość:', nx.closeness_centrality(G))
# print('Pośrednictwo:', nx.betweenness_centrality(G))
# print('Średnia:', nx.diameter(G))
# for z in nx.connected_components(G):
#     print('Składowa spójna:', z)
# k = 3
# print('Sprawdzam spójność grafu dla k =:', k, nx.is_k_edge_connected(G, k))
# print('Spójność krawędziowa:', nx.edge_connectivity(G))
# print('Spójność wierzchołkowa:', nx.node_connectivity(G))
# print('Średnia długość ścieżki:', nx.average_shortest_path_length(G))




# print('Wszystkie kliki >=3:')
# i = 1
# for z in nx.enumerate_all_cliques(G):
#     if len(z) >= 3:
#         print(i, z)
#         i = i + 1
# print('Kliki maksymalne:')
# i = 1
# for z in nx.find_cliques(G):
#     if len(z) >= 3:
#         print(i, z)
#         i = i + 1
#         K = nx.Graph()
#         K.nodes(data=True)
#         K.add_nodes_from(z)
#         connections = []
#         for t in range(len(z)):
#             for r in range(len(z)):
#                 connections.append((z[t],z[r]))
#         # print(connections)
#         K.add_edges_from(connections)
#         nx.draw_spring(K, with_labels=True)
#         plt.show()

# print(nx.to_numpy_matrix(G))
# print(nx.incidence_matrix(G))
hist_list = []

for i in range(max(nx.degree(G))[1]+1):
    hist_list.append([0,i+1])

for i in nx.degree(G):
    temp = list(i)[1]
    hist_list[temp-1][0] += 1

height = []
bars = []
for i in hist_list:
    height.append(i[0])
    bars.append(i[1])

y_pos = np.arange(len(height))
 
plt.figure(figsize=(10,5))

plt.bar(y_pos, height, color = '#969696')
  
plt.xticks(y_pos, bars)
 
plt.xlabel('Ilość węzłów', fontsize=12, color='#323232')
plt.ylabel('Ilość wierzchołków', fontsize=12, color='#323232')
plt.title('Histogram stopni wierzchołków', fontsize=16, color='#323232')


xmin = min(hist_list)[0]
suma = 0

for i in range(len(hist_list)):
    suma = suma + m.log(hist_list[i][0])

alfa = 1 + m.pow((-m.log(xmin) + 1/len(hist_list)*suma),-1)

print(alfa)
plt.show()