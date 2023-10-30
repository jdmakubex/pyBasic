import pandas as pd

'''
el método loc, sirve para extraer o mostrasr una fina, pasandole como parametro el índice
de tipo string que quieres mostrar

'''
usuarios = {
    'username' : ['user1','user2','user3','user4','user5'],
    'email' : ['user1@example.com','user2@example.com','user3@example.com','user4@example.com','user5@example.com'],
    'age' : [10,20,25,30,50],
    'status' : [True,True,False,False,True]
}

df  = pd.DataFrame(usuarios, index=['a','b','c','d','e'])
print(df)

print('\n Extrae datos de la fila "a" \n', df.loc['a']);

print('\n Genera un subdataframe con las primeras 3 filas \n');
sdf = df.loc['a':'c'];
print(sdf);

print('\n Genera un subdataframe con las primeras 3 filas, y solo las columnas username e email \n');
sdf = df.loc['a':'c',['username','email']];
print(sdf);