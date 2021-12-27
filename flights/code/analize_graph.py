import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/small_sample_delays_only.csv')

edge_list=[]

for i in range(len(df)):
    if [df.iloc[i]['ORIGIN_AIRPORT'],df.iloc[i]['DESTINATION_AIRPORT']] not in edge_list and [df.iloc[i]['DESTINATION_AIRPORT'],df.iloc[i]['ORIGIN_AIRPORT']] not in edge_list:
        edge_list.append([df.iloc[i]['ORIGIN_AIRPORT'],df.iloc[i]['DESTINATION_AIRPORT']])

print(df)

G = nx.Graph()
G.add_nodes_from(df['ORIGIN_AIRPORT'])
G.add_edges_from(edge_list)
nx.draw_kamada_kawai(G, with_labels=True)
# plt.show()

print('\nŚrednica: ',nx.diameter(G))
print('\nGęstość: ',nx.density(G))
st = pd.DataFrame(nx.degree(G))
cols = ['AIRPORT','CONNECTIONS']
st.columns = cols
print('\nTop 5 lotnisk z największą ilością połączeń:\n\n',st.sort_values(by='CONNECTIONS', ascending=False).head(5).reset_index())