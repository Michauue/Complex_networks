import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/small_sample_delays_only.csv')

edge_list=[]

for i in range(len(df)):
    if [df.iloc[i]['ORIGIN_AIRPORT'],df.iloc[i]['DESTINATION_AIRPORT']] not in edge_list and [df.iloc[i]['DESTINATION_AIRPORT'],df.iloc[i]['ORIGIN_AIRPORT']] not in edge_list:
        edge_list.append([df.iloc[i]['ORIGIN_AIRPORT'],df.iloc[i]['DESTINATION_AIRPORT']])
    if i % 10000 == 0:
        print(i)
print(df)

G = nx.Graph()
G.add_nodes_from(df['ORIGIN_AIRPORT'])
G.add_edges_from(edge_list)
# nx.draw_kamada_kawai(G, with_labels=True)
# plt.show()

print('\nŚrednica (najdłuższa z najkrótszych ścieżek): ',nx.diameter(G))
print('\nGęstość: ',nx.density(G))
print('\nIlość wierzchołków: ',G.number_of_nodes())
print('\nRozmiar (ilość połączeń): ',G.size())

edge_cen = pd.DataFrame.from_dict(nx.edge_betweenness_centrality(G), orient='index')
cols_1 = ['EDGE_BETWEENNESS_CENTRALITY']
edge_cen.columns = cols_1
print('\nTop 5 połączeń z największym współczynnikiem centralności:\n\n',edge_cen.sort_values(by='EDGE_BETWEENNESS_CENTRALITY', ascending=False).head(5).reset_index())

eig_cen = pd.DataFrame.from_dict(nx.eigenvector_centrality(G), orient='index')
cols_2 = ['EIGENVECTOR_CENTRALITY']
eig_cen.columns = cols_2
print('\nTop 5 lotnisk z największym współczynnikiem centralności wektora własnego:\n\n',eig_cen.sort_values(by='EIGENVECTOR_CENTRALITY', ascending=False).head(5).reset_index())

st_cen = pd.DataFrame.from_dict(nx.degree_centrality(G), orient='index')
cols_3 = ['DEGREE_CENTRALITY']
st_cen.columns = cols_3
print('\nTop 5 lotnisk z największym współczynnikiem centralności:\n\n',st_cen.sort_values(by='DEGREE_CENTRALITY', ascending=False).head(5).reset_index())

st = pd.DataFrame(nx.degree(G))
cols_4 = ['AIRPORT', 'CONNECTIONS']
st.columns = cols_4
print('\nTop 5 lotnisk z największą ilością połączeń:\n\n',st.sort_values(by='CONNECTIONS', ascending=False).head(5).reset_index())

# python_file = open("example.txt", "a")

print('\nKliki maksymalne k>=8:\n')
for i in nx.enumerate_all_cliques(G):
    if len(i) > 7:
        print(i)
        # i = str(i)+'\n'
        # python_file.write(i)
        # K = nx.complete_graph(i)
        # nx.draw_kamada_kawai(K, with_labels=True)
        # plt.show()

# python_file.close()