import pandas as pd


def merge(df, chosen_airline):
    airlines = pd.read_csv('../dataset/airlines.csv')

    my_airline = chosen_airline
    my_airline_airports = []
    tab = []
    compare_tab =  []
    final_tab = []
    max_diversity = 0
    save_index = 0

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
    airlines_tab.remove(my_airline)

    for i in range(len(airlines_tab)):
        if airlines_tab[i] == my_airline:
            airlines_tab[i] = 'next'

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
    
    for j in range(len(tab)):
        compare_tab.append(list(set(my_airline_airports).intersection(set(tab[j]))))
        diversity = len(tab[j]) - len(compare_tab[j])
        if diversity > max_diversity:
            max_diversity = diversity
            save_index = j

    for i in range(len(tab[save_index])):
        if tab[save_index][i] not in compare_tab[save_index]:
            final_tab.append(tab[save_index][i])

    return my_airline_airports, final_tab

# print('\nLiczba obsługiwanych lotnisk przed połączeniem z linią', airlines_tab[save_index], ':', len(my_airline_airports))
# print('Liczba obsługiwanych lotnisk po połączeniu z linią', airlines_tab[save_index], ':', len(my_airline_airports)+len(final_tab))
# print('\nNowe lotniska:',final_tab)
# print()
