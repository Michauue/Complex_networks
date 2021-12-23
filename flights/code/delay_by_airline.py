import pandas as pd
import numpy as np
import time
import pandas_profiling
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def my_colours(n):
    colours = ['aquamarine', 'burlywood', 'darksalmon', 'limegreen', 'aliceblue', 'tomato', 'lightskyblue', 'violet', 'wheat', 'sandybrown', 'orange', 'gold', 'lightcoral', 'snow', 'darkorchid',
               'royalblue', 'teal', 'hotpink', 'chocolate', 'palegreen', 'steelblue', 'peru', 'khaki', 'mediumslateblue', 'novajowhite', 'cornflowerblue', 'moccasin', 'mediumseagreen', 'powderblue', 'rosybrown']
    tab = colours[0:n]
    return tab

df = pd.read_csv('../dataset/delays_only.csv')
airlines = pd.read_csv('../dataset/airlines.csv')

df_delay = df[df.DEPARTURE_DELAY >= 1]
dep_delayed_flights = df_delay.groupby(['AIRLINE'], as_index=False).agg({'DEPARTURE_DELAY': 'mean'})

print(dep_delayed_flights)

matrix = dep_delayed_flights['AIRLINE']
matrix2 = dep_delayed_flights['DEPARTURE_DELAY']
length = np.arange(len(matrix2))

plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor('dimgray')
plt.bar(length, matrix2, color=my_colours(len(matrix2)))
plt.xticks(length, matrix)
plt.savefig('barplot.png')

# f,ax = plt.subplots(figsize=(10, 8))
# sns.barplot(dep_delayed_flights)
# ax.set_title('Airline Departure Delay Distribution', fontsize=16)
# ax.set_ylabel("Departure Delay", fontsize=16)
# ax.set_xlabel("Airlines", fontsize=16)
# plt.close(2)
# plt.show()