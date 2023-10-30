import pandas as pd
'''
Operadores condicionales y operadores lógicos.
'''

print('\n Leemos los datos desde un CSV  \n');
df = pd.read_csv('./input/incompletos.csv', index_col='id');
print(df);

print('\n Limpiaremos los datos, eliminando las filas donde hay valores nulos \n');
df = df.dropna();
print(df);

print('\n Obtener el nombre de todos los usuarios del pais Canadá \n');

uc = df[df['pais'] == 'Canada'] ['nombre'];
print(uc);

print('\n Obtener el nombre y correo de todos los usuarios con edad mayor a 50  \n');
nc = df[df['edad'] > 50 ][ ['nombre','email'] ];
print(nc);

print('\n Obtener el promedio de todos los usuarios de sexo femenino con una edad mayor a 30 \n');
puxf = df[ (df['genero'] == 'female')&(df['edad']>30)]['edad'].mean()
print(puxf);