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

print('\n Obtener todos los usuarios entre las edades 40 y 50 \n');
# ue = df [(df['edad'] >=40) & (df['edad']<=50)]; #Otra forma de resolverlo
ue = df [df ['edad'].between(40,50)];
print(ue);

