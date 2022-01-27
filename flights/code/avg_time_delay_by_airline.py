import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colours import my_colours

df = pd.read_csv('../dataset/sample_delays_only_v3.csv')
airlines = pd.read_csv('../dataset/airlines.csv')

# wykres średniego czasu opóźnienia (jeżeli wystąpiło), z podziałem na linie lotnicze 

df_delay = df[df.DEPARTURE_DELAY >= 1]
dep_delayed_flights = df_delay.groupby(['AIRLINE'], as_index=False).agg({'DEPARTURE_DELAY': 'mean'})
dep_delayed_flights['DEPARTURE_DELAY'] = dep_delayed_flights['DEPARTURE_DELAY'].round(decimals=2)
print(dep_delayed_flights)

matrix = dep_delayed_flights['AIRLINE']
matrix2 = dep_delayed_flights['DEPARTURE_DELAY']
length = np.arange(len(matrix2))

plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor('dimgray')
plt.bar(length, matrix2, color=my_colours(len(matrix2)))
plt.xticks(length, matrix)
plt.show()
