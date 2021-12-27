import pandas as pd
import networkx as nx
from pandas.core import indexing

df = pd.read_csv('../dataset/delays_only_v3.csv')
df = df.drop(columns=['Unnamed: 0', 'level_0', 'Unnamed: 0.1', 'index'])
df = df.sample(n=500000, random_state=254279).sort_index().reset_index()
df = df.drop(columns=['index'])
df.to_csv('../dataset/sample_delays_only_v3.csv')
