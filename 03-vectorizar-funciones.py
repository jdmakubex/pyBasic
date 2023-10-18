import numpy as np

def operacion (valor):
    return(valor**2)+2

print('\n Genera un arreglo de 20 elementos, con numero aleatorios entre 0 y 10 \n');
a = np.random.randint(0,10,20)
print(a)

print('\n Implementa la función en cada valor del arreglo \n');
vector = np.vectorize(operacion)
r = vector(a)
print(r)

print('\n Utilizando la función lambda \n');
vector = np.vectorize(lambda valor:(valor**2)+2)
r = vector(a)
print(r)