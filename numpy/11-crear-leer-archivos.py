import numpy as np

'''
save: Guarda archivos binarios
load: Carga arrchivos binarios.
savetxt: Guarda archivos planos
loadtxt: Carga archivos planos
NOTA: por convención los archivos binarios de numpy se guartar con extension: .npy
'''

print('\n Creamos un arreglo de 10 con numero aleatorios: \n');
a = np.random.randint(0,10,10);
print(a);

print('\n Almacenamos los valores del arreglo en un archivo plano: \n');
#Argumentos: path, arreglo, formato de dato
np.savetxt('./out/arreglo.txt', a, fmt='%i');

print('\n Leer datos desde un archivo: \n');
#Argumentos: path, arreglo, formato de dato
b = np.loadtxt('./out/arreglo.txt', dtype=int, delimiter = ',' )
print(b);


print('\n Retomemos el arreglo a: \n');
print(a);
print('\n Redimencionemos el arreglo como una matriz "c" de 2 x 5: \n');
c = a.reshape(( 2,5 ));
print(c);
print('\n Guardamos los datos en el archivo matriz.csv: \n');
np.savetxt('./out/matriz.csv', c, fmt='%i', delimiter=',');

print('\n Leer datos desde un archivo matriz.csv y lo guardamos en "l": \n');
l = np.loadtxt('./out/matriz.csv',delimiter=',', dtype=int);
print(l);

#Trabajando con archivos binarios
print('\n Guardamos los datos en el archivo arreglo_binario.npy: \n');
np.save('./out/arreglo_binario.npy', a);
print('\n Leemos el archivo binario arreglo_binario.npy: \n');
rb = np.load('./out/arreglo_binario.npy');
print(rb)







