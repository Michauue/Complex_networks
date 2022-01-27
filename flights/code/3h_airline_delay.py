import pandas as pd
from colours import my_colours
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../dataset/sample_delays_only_v3.csv')
airlines = pd.read_csv('../dataset/airlines.csv')

# wykres ilości opóźnień wynoszących powyżej 3h z podziałem na linie lotnicze

hour_delay = df.loc[df['DEPARTURE_DELAY'] > 180].reset_index()
hour_delay = hour_delay.loc[hour_delay['ARRIVAL_DELAY'] > 180]
airline_to_delay = hour_delay.groupby(['AIRLINE']).count().sort_values('YEAR',ascending=True).reset_index()

tab = list(airline_to_delay['AIRLINE'].values)

length = np.arange(len(airline_to_delay['AIRLINE'].values))
plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor('dimgray')
plt.bar(length, airline_to_delay['index'].values, color=my_colours(len(airline_to_delay['AIRLINE'].values)))
plt.xticks(length, airline_to_delay['AIRLINE'].values)
plt.title('Liczba ponad 3 godzinnych opóźnień z podziałem na linie lotnicze')
plt.show()


df = df.groupby(['AIRLINE']).count().sort_values(by='MONTH', ascending=False).reset_index()
df = df.drop(columns=df.iloc[:,1:-1])
cols_df = ['AIRLINE', 'TOTAL_FLIGHTS']
df.columns = cols_df
new = pd.merge(df,airline_to_delay)
cols_new = ['AIRLINE', 'TOTAL_FLIGHTS', '3H_DELAY_FLIGHTS']
new = new.drop(columns=new.iloc[:,2:-1])
new.columns = cols_new
new['RATIO'] = round(new['3H_DELAY_FLIGHTS']/new['TOTAL_FLIGHTS']*100,2)
new = new.sort_values(by='RATIO', ascending=False).reset_index()
new = new.drop(columns=['index'])
print(new)