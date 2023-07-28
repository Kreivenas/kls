import pandas as pd
import numpy as np

df = pd.read_csv('miestai_isvalyti.csv')
# print(df.head(5))
# df.set_index('Miestas', inplace=True)
# print(df)
# gyventojos = df.loc[df['Miestas'] == 'Marijampolė', '1923']
# print(gyventojos)
# stulpelis_1897 = df['1897'].head(5)v66 v
# print(stulpelis_1897)
# stulpeliai = ['2019', '1970', '1923']
# eilutes = df.head(10)
# stulpeliai_eilutes = eilutes[stulpeliai]
# print(stulpeliai_eilutes)
eiluciu_skaicius = df.shape[0]
print(eiluciu_skaicius)

