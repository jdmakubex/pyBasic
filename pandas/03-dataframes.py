import pandas as pd
'''
Un Dataframe, es una estructura de datos similar a una hora de excel, conformado
por filas y columas. La forma mas facil de crear un dataframe es a travéz de un un diccionario.
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

print('\n Personalizando los índices \n');
df = pd.DataFrame(usuarios, index=['a','b','c']);
print(df);

print('\n Para obtener la columna de edades del dataframe:  \n');
print(df['age']);

print('\n Para obtener una edad especifica del dataframe \n');
print(df['age']['a']);

print('\n Otra forma de acceder a los datos de un dataframe: df.email \n');
print(df.email)

print('\n Para ver el nombre de las columnas que componen el dataframe \n');
print(df.columns)

print('\n Para ver los valores de las columnas que componen el dataframe \n');
print(df.values)