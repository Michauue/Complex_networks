import pandas as pd

# rekordy z października zawierały liczby w polach lotnisk, stad wyrzucam ten miesiąc z analizy

df = pd.read_csv('../dataset/delays_only_v2.csv')

df = df.drop(index=df[df["MONTH"] == 10].index)
df = df.reset_index()

df.to_csv('../dataset/delays_only_v3.csv')
