import numpy as np

print('Creamos un arreglo de dimención 20, con numeros aleatorios de 0 al 10: ');
a = np.random.randint(0,10,20);
print(a);

#Ejemplo de sort()
print('\n Ordenamiento Ascendente \n');
a = np.sort(a);
print(a);

#Ejemplo de Ordenamiento Descendente
print('\n Ordenamiento Descendente \n');
a = a [::-1]
print(a);