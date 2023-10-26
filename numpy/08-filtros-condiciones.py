import numpy as np

a = np.random.randint(0,100,50);
print('Creamos un arreglo: \n',a)

print('\n condicionando el arreglo:  a > 50 \n', a > 50)

print('\n Obteniendo solo los valores que cumplen con la condicion:  a[a > 50] \n', a[a > 50])

print('\n Valores que cumplen con la condicion:  a[(a > 50) & (a < 90)] \n', a[(a > 50) & (a < 90)])


print('\n Valores que cumplen con la condicion:  a[(a == 10) | (a == 20) | (a == 30)] \n', a[(a == 10) | (a == 20) | (a == 30)])