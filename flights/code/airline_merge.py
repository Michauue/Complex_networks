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


airlines_tab = list(airlines['IATA_CODE'].values)

print(airlines_tab)

for i in range(len(airlines_tab)):
    if airlines_tab[i] == my_airline:
        airlines_tab[i] = 'next'
    
print(len(airlines_tab))

tab = []

for j in range(len(airlines_tab)):
    if airlines_tab[j] == 'next':
        continue
    tab.append([])
    for i in range(len(df)):
        temp_airline = df.iloc[i]['AIRLINE']
        if temp_airline == airlines_tab[j]:
            origin = df.iloc[i]['ORIGIN_AIRPORT']
            destination = df.iloc[i]['DESTINATION_AIRPORT']
            if origin not in tab[j-1]:
                tab[j-1].append(origin)
            if destination not in tab[j-1]:
                tab[j-1].append(destination)

print(tab)