import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/small_sample_delays_only.csv')
airports = pd.read_csv('../dataset/airports.csv')
airlines = pd.read_csv('../dataset/airlines.csv')

temp = df.groupby(['AIRLINE']).count()

my_airline_airports = []
my_airline = 'WN'

for i in range(len(df)):
    temp_airline = df.iloc[i]['AIRLINE']
    if temp_airline == my_airline:
        origin = df.iloc[i]['ORIGIN_AIRPORT']
        destination = df.iloc[i]['DESTINATION_AIRPORT']
        if origin not in my_airline_airports:
            my_airline_airports.append(origin)
        if destination not in my_airline_airports:
            my_airline_airports.append(destination)

print(len(my_airline_airports))


