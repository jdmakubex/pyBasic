import pandas as pd
import numpy as np

'''
Las columnas, son series, para añadir nuevas columnas, debemos crear una serie nueva.
'''
print('\n Creamos un objeto tipo diccionario \n');
usuarios = {
    'username' : ['user1', 'user2', 'user3'],
    'email' : ['user1@example.com', 'user2@example.com', 'user3@example.com'],
    'age' : [20,10,30],
    'status' : [True,True,False]
}
df = pd.DataFrame(usuarios);
print(df);

# columna =  serie

print('\n Creamos una serie nueva llamada calificaciones  \n');
calificaciones = pd.Series (np.random.randint(5,10,3))
print(calificaciones)

print('\n Agregamos al dataframe la columna calificaciones  \n');
df['calificaciones'] = calificaciones;
print(df);

print('\n Renombramos la columna "calificiaciones" \n');
df = df.rename(
    columns={'calificaciones':'score'}
)
print(df);

print('\n Elimina la columna score: " \n');
del df['score'];
print(df);