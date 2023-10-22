import numpy as np

print('\n Creamos una matriz de 3 x 5 \n');
A = np.array([
    [1,2,3,4,5],
    [10,20,30,40,50],
    [100,200,300,400,500]
]);
print(A)

print('\n Conocer las dimenciones de un arreglo con .ndim \n');
print(A.ndim)

print('\n Conocer la forma de un arreglo con .shape \n');
print(A.shape)

print('\n Obtener el primer elemento de la matriz, posiscion 0,0 \n');
print(A[0,0]);

print('\n Obtener el ultimo elemento de la matriz, posiscion 2,4 \n');
print(A[2,4]);

print('\n Para formar un sub arreblo de a partir de los primeros 3 elementos');
print('de la segunfa fila A[1, :3');
print(A[1, :3]);

print('\n Para formar un sub arreblo de a partir de los 3 ultimos elementos');
print('de la tercera fila A[2, 2:]');
print(A[2, 2:]);

print('\n Obtener el primero y ultimo elemento de la primera fila');
print(' A[0, [0,4]]');
print(A[0, [0,4]]);

print('\n Imprime todos los elementos de la columna 3');
print(' A[ : ,3] ');
print('\n',A,'\n')
print(A[ : ,3]);

print('\n Imprime el primero y ultimo elemento de la columna 3');
print(' A[[0,2]: ,3 ');
print('\n',A,'\n')
print(A[[0,2] ,3]);