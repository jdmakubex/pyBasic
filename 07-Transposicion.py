'''
La transposición de una matriz, consiste en convertir las filas a columnas y 
las columnas en filas.
'''

import numpy as np

print('\n Creamos una matriz de 3 x 5 \n');
A = np.array([
    [1,2,3,4,5],
    [10,20,30,40,50],
    [100,200,300,400,500]
]);
print(A)

print('\n Aplicando transposición a la matriz A \n');
print(A.T)


print('\n Sumaremos la ultima columna de la matriz original:  \n');
print(A)
print('\n A[:,4].sum() es: ', A[:,4].sum());

print('\n Aplicando transpuesta y sumando:  \n');
print(A.T)
print('\n A.T[4].sum() es: ', A.T[4].sum());
