import pandas as pd

print('\n Leemos los datos desde un CSV  \n');
df = pd.read_csv('./input/incompletos.csv', index_col='id');
print(df);

print('\n Limpiaremos los datos, eliminando las filas donde hay valores nulos \n');
df = df.dropna();
print(df);

print('\n Muestra la cantidad de hombres y mujeres del dataset \n');
r = df.groupby('genero')['genero'].count();
print(r);

print('\n Muestra el país con mas mujeres \n');
r = df[df['genero']=='female'].groupby('pais')['pais'].count().sort_values(ascending=False).head(1);
print(r);