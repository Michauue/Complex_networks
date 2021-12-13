import networkx as nx
import matplotlib.pyplot as plt

drivers = ['Alonso', 'Leclerc', 'Hamilton', 'Vettel', 'Perez', 'Sainz',
           'Raikkonen', 'Ricciardo', 'Verstappen', 'Kviat', 'Kubica',
           'Massa', 'Button', 'Hulkenberg', 'Barrichello', 'Schumacher',
           'Heidfeld', 'Bottas']

relations = [('Alonso', 'Hamilton'), ('Alonso', 'Massa'), ('Alonso', 'Raikkonen'),('Alonso', 'Button'),
            ('Leclerc', 'Vettel'), ('Leclerc', 'Sainz'),
            ('Hamilton','Alonso'),('Hamilton','Button'),('Hamilton','Bottas'),
            ('Vettel','Heidfeld'),('Vettel','Kubica'),('Vettel','Ricciardo'),('Vettel','Raikkonen'),('Vettel','Leclerc'),
            ('Perez','Verstappen'),('Perez','Hulkenberg'),('Perez','Button'),
            ('Sainz','Verstappen'),('Sainz','Hulkenberg'),('Sainz','Kviat'),('Sainz','Leclerc'),
            ('Raikkonen','Massa'),('Raikkonen','Alonso'),('Raikkonen','Vettel'),('Raikkonen','Giovinazzi'),
            ('Ricciardo','Hulkenberg'),('Ricciardo','Kviat'),('Ricciardo','Verstappen'),('Ricciardo','Vettel'),
            ('Verstappen','Kviat'),('Verstappen','Ricciardo'),
            ('Kviat','Verstappen'),('Kviat','Ricciardo'),('Kviat','Sainz'),
            ('Kubica','Heidfeld'),('Kubica','Vettel'),('Kubica','Russell'),
            ('Massa','Schumacher'),('Massa','Raikkonen'),('Massa','Alonso'),('Massa','Bottas'),
            ('Button','Alonso'),('Button','Hamilton'),('Button','Barrichello'),('Button','Perez'),
            ('Hulkenberg','Ricciardo'),('Hulkenberg','Barrichello'),('Hulkenberg','Sainz'),('Hulkenberg','Perez'),
            ('Barrichello','Hulkenberg'),('Barrichello','Schumacher'),('Barrichello','Button'),
            ('Schumacher','Barrichello'),('Schumacher','Massa'),
            ('Heidfeld','Kubica'),('Heidfeld','Vettel'),
            ('Bottas','Massa'),('Bottas','Hamilton'),
            ('Giovinazzi','Raikkonen'),
            ('Russell','Kubica')]


G = nx.Graph()
G.add_nodes_from(drivers)
G.add_edges_from(relations)
nx.draw(G, with_labels=True)
print('Rząd:',G.number_of_nodes())
print('Rozmiar:',G.size())
print('Stopień wierzchołków:',nx.degree(G))
print('Gęstość:',nx.density(G))
print('Bliskość:', nx.closeness_centrality(G))
print('Pośrednictwo:', nx.betweenness_centrality(G))
print('Średnia:', nx.diameter(G))
for z in nx.connected_components(G):
    print('Składowa spójna:', z)
k=3
print('Sprawdzam spójność grafu dla k =:',k,nx.is_k_edge_connected(G,k))
print('Spójność krawędziowa:',nx.edge_connectivity(G))
print('Spójność wierzchołkowa:',nx.node_connectivity(G))
print('Średnia długość ścieżki:',nx.average_shortest_path_length(G))
for z in nx.find_cliques(G):
    print(z)
# plt.savefig('graph.png')
