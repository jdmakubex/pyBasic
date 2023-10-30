import pandas as pd

'''
El método iloc, funciona parecido que el método loc,
solo que trabaja con índices de tipo entero.
'''
print('\n Leemos los datos desde un CSV  \n');
df = pd.read_csv('./input/incompletos.csv', index_col='id');
print(df);

print('\n Extrae datos de la fila 0 \n', df.iloc[0]);
print('\n Extrae datos de la ultima fila  \n', df.iloc[199]);

print('\n Construye un sub data frame con los primeros registros del DF  \n');
sdf = df.iloc[:5]
print(sdf);

print('\n Construye un sub data frame con los primeros registros del DF  \n');
print(' y solo las columnas name, gender y email  \n');
sdf = df.iloc[:5,[0,2,4]] #Las columas también se pueden asociar a indices según su orden
print(sdf);

#Otrea forma de lograr el mismo resultado:
print('\n Otra forma de lograr el mismo resultado  \n');
print('es poniendo el nombre de las columas directamente  \n');
sdf = df.iloc[:3][ ['nombre', 'genero', 'email'] ] #Se logra nombrando el nombre de las columnas
print(sdf);
#Este ejemplo es mas legible y se recomienda más

