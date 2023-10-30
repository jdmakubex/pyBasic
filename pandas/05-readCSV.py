import pandas as pd

'''
En este escript, se ejemplifica como formar un datafreame, a partir de atos extraídos 
de un CSV.
'''

print('\n Leemos los datos desde un CSV  \n');
df = pd.read_csv('./input/users.csv');
print(df);

print('\n Hacemos que la columna id sean los indices del dataframe  \n');
df = pd.read_csv('./input/users.csv', index_col='id');
print(df);

'''
Los métodos :
1. head() : Muestra los primeros registros del DF
2. tail() : Muestrea los ultimos registro del DF
'''

print('\n Muestra el ultimo los ultimos 10 registros del DF  \n', df.tail(10));