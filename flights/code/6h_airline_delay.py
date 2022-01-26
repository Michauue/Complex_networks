import pandas as pd
from colours import my_colours
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/sample_delays_only_v3.csv')
airlines = pd.read_csv('../dataset/airlines.csv')

# wykres ilości opóźnień wynoszących powyżej 6h z podziałem na linie lotnicze

hour_delay = df.loc[df['DEPARTURE_DELAY'] > 300].reset_index()
hour_delay = hour_delay.loc[hour_delay['ARRIVAL_DELAY'] > 300]
airline_to_delay = hour_delay.groupby(['AIRLINE']).count().sort_values('YEAR',ascending=True).reset_index()

print(airline_to_delay['AIRLINE'].values,airline_to_delay['index'].values)

length = np.arange(len(airline_to_delay['AIRLINE'].values))
plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor('dimgray')
plt.bar(length, airline_to_delay['index'].values, color=my_colours(len(airline_to_delay['AIRLINE'].values)))
plt.xticks(length, airline_to_delay['AIRLINE'].values)
plt.show()
