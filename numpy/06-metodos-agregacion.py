import numpy as np

print('\n Creamos una matriz de 3 x 5 \n');
A = np.array([
    [1,2,3,4,5],
    [10,20,30,40,50],
    [100,200,300,400,500]
]);
print(A)

print('\n Saber la desviación estándart del arreglo con: .std() \n');
print('la desviación estándar del arreglo es: ',A.std())

print('\n Saber la suma total de todos los elementos de arreglo con: .sum() \n');
print('la suma de todos los elementos del arreglo es: ',A.sum())

print('\n Saber el valor mínimo de todos los elementos de arreglo con: .min() \n');
print('El valor mínimo de todos los elementos del arreglo es: ',A.min())

print('\n Saber el valor máximo de todos los elementos de arreglo con: .max() \n');
print('El valor máximo de todos los elementos del arreglo es: ',A.max())

print('\n Saber el promedio del arreglo con: .mean() \n');
print('El promedio del arreglo es: ',A.mean())

print('\n Suma todo los elementos de la fila 2. A[1] \n');
print('Total de la suma de los elementos de A[1] =', A[1].sum())

print('\n Saber el valor mínimo de los elementos de la fila 3 \n');
print('El valor mínimo de todos los elementos del arreglo es: ',A[2].min())

print('\n Saber el valor máximo de los elementos de la fila 3 \n');
print('El valor máximo de todos los elementos del arreglo es: ',A[2].max())

print('\n Obtener el promedio de la columna 3 \n');
print('El de los elementos de la columna 3 es : ',A[:,2].mean())

print('\n Obtener el promedio de la columna 4 \n');
print('El de los elementos de la columna 4 es : ',A[:,3].mean())