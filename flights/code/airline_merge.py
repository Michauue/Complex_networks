from typing import final
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/small_sample_delays_only.csv')
airports = pd.read_csv('../dataset/airports.csv')
airlines = pd.read_csv('../dataset/airlines.csv')

temp = df.groupby(['AIRLINE']).count()

my_airline_airports = []
my_airline = 'MQ'

for i in range(len(df)):
    temp_airline = df.iloc[i]['AIRLINE']
    if temp_airline == my_airline:
        origin = df.iloc[i]['ORIGIN_AIRPORT']
        destination = df.iloc[i]['DESTINATION_AIRPORT']
        if origin not in my_airline_airports:
            my_airline_airports.append(origin)
        if destination not in my_airline_airports:
            my_airline_airports.append(destination)


airlines_tab = list(airlines['IATA_CODE'].values)

print('\nWszyskie linie lotnicze:', airlines_tab)

airlines_tab.remove(my_airline)


for i in range(len(airlines_tab)):
    if airlines_tab[i] == my_airline:
        airlines_tab[i] = 'next'
    
print('Linie lotnicze bez mojej linii:', airlines_tab)

tab = []

for j in range(len(airlines_tab)):
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


compare_tab =  []
max_diversity = 0
save_index = 0
final_tab = []

for j in range(len(tab)):
    compare_tab.append(list(set(my_airline_airports).intersection(set(tab[j]))))
    diversity = len(tab[j]) - len(compare_tab[j])
    if diversity > max_diversity:
        max_diversity = diversity
        save_index = j

for i in range(len(tab[save_index])):
    if tab[save_index][i] not in compare_tab[save_index]:
        final_tab.append(tab[save_index][i])

print('\nLiczba obsługiwanych lotnisk przed połączeniem z linią', airlines_tab[save_index], ':', len(my_airline_airports))
print('Liczba obsługiwanych lotnisk po połączeniu z linią', airlines_tab[save_index], ':', len(my_airline_airports)+len(final_tab))
print('\nNowe lotniska:',final_tab)
print()