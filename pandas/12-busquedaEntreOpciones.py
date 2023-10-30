import pandas as pd
'''
Búsqueda por rango
'''

print('\n Leemos los datos desde un CSV  \n');
df = pd.read_csv('./input/incompletos.csv', index_col='id');
print(df);

print('\n Limpiaremos los datos, eliminando las filas donde hay valores nulos \n');
df = df.dropna();
print(df);

print('\n Obtener el nombre de todos los usuarios mayores a 30 años de los países Canadá, Alemania y Francia \n');
#Esta opción no es muy optima
#r = df[(df ['edad']>30)&( (df['pais'] == 'Canada') | (df['pais'] == 'Germany') | (df['pais'] == 'France'))]
'''
Una opción más legible, y optima:
'''

countries = ['Canada','Germany','France'];
r = df[(df['edad']>30)&(df['pais'].isin(countries))]
print(r);



