import pandas as pd

print('\n Leemos los datos desde un CSV  \n');
df = pd.read_csv('./input/incompletos.csv', index_col='id');
print(df);

'''
En numpy y pandas, la forma en que se respresenta la ausencia de algún valor es NaN. 
Por lo tanto la estrategia a seguir será:
1. Eliminar los registros con valores NaN
o 
2. Reemplazar los valores NaN por valores por defecto
'''

df = df.dropna();
print(df);

#Cargamos de nuevo los datos incompletos
print('\n Leemos  de nuevo los datos desde un CSV  \n');
df = pd.read_csv('./input/incompletos.csv', index_col='id');

print('\n Se reemplaza la ausencia se valor por la leyenda "Sin Dato"  \n');
df = df.fillna('Sin Dato');
print(df);


#Personalizando más el rellenado de datos vacíos
print('\n Leemos  de nuevo los datos desde un CSV  \n');
df = pd.read_csv('./input/incompletos.csv', index_col='id');

print('\n Se reemplaza la ausencia de valor por valores acorde a cada columna  \n');
df = df.fillna( { 'nombre' : 'Sin Nombre', 'email' : 'example@example.com' } );
print(df);

