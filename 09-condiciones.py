import numpy as np

'''
.all/(): Retorna verdadero si todos los elementos cumplen la condición
.any(): Retorna verdadero si por lo menos un elemento cumple con la condición.
'''

a = np.random.randint(0,100,50);
print('Creamos un arreglo: \n',a)

print('\n Saber si todos los elementos son mayores a 50: np.all( a > 50)  \n', np.all(a > 50));

print('\n Saber si todos los elementos son mayores o igual a 0: np.all( a >= 0)  \n', np.all(a >= 0));

print('\n Saber si se cumple la condición: np.all(( a >= 0) & ( a <= 100))  \n', np.all(( a >= 0) & ( a <= 100)));

print('\n Saber si al menos un elementos es mayor a 10: np.any( a > 10)  \n', np.any(a > 10));