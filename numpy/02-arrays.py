import numpy as np

'''
Ejemplo de Sub arreglos
'''
print('\n Genera un arreglo de 20 elementos, con numero aleatorios entre 0 y 10 \n');
a = np.random.randint(0,10,20)
print(a)

print('\n Obtener un subarreglo de los primeros 5 elementos del arreglo original \n');
sa1 = a[:5]
print(sa1)

'''
La estructura parea generar esto es la siguiente:

a[start:end:saltos]

'''

print('\n Obtener un subarreglo con los elementos en posicion 0,1 y 3 del arreglo original \n');
sa2 = a[[0,1,3]]
print(sa2)

print('\n === \n');
print('\n Genera un arreglo de 5 elementos, con numero aleatorios entre 0 y 10 \n');
b = np.random.randint(0,10,5)
print(b)

print('\n Genera un subarreglo, con el primer y ultimo elemento del arreglo \n');
sa3 = b[ [True, False, False, False, True]]
print(sa3)