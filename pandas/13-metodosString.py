import pandas as pd
'''
Métodos para tratamiento de strings:
1. startswith: Comienza con
2. endswith: Termina con
3. contains: Contiene
'''

print('\n Leemos los datos desde un CSV  \n');
df = pd.read_csv('./input/incompletos.csv', index_col='id');
print(df);

print('\n Limpiaremos los datos, eliminando las filas donde hay valores nulos \n');
df = df.dropna();
print(df);


print('\n Imprime los usuarios cuyo correo electrónico empiece con "a" \n');
r = df[df['email'].str.startswith('a')]
print(r);

print('\n Imprime los usuarios cuyo correo electrónico termine con ".com" \n');
r = df[df['email'].str.endswith('.com')]
print(r);

print('\n Imprime los usuarios cuyo nombre contiene "Gabriel" \n');
r = df[df['nombre'].str.contains('Gabriel')]
print(r);

