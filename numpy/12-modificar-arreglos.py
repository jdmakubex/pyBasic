import numpy as np

'''
En teoría, normalmente, durante la ejecusión de un escript, un arreglo no debería 
cambiar su dimensión, para hacerlo hay procedimientos especiales, 
los cuales se ejemplifica en en este escript.

El hecho de que un arreglo tenga una longitud fija, da mas rapidez a su lectura.
'''

print('Creamos un arreglo de dimención 10, con numeros aleatorios de 0 al 10: ');
a = np.random.randint(0,10,10);
print(a);

print('\n Elementos del arreglo: ', a.size);

'''
Para agregar mas elementos al arreglo, y por lo tanto modificar su logitud se hace 
con las funciones: 
1. insert: Pasando como parametros, el arreglo, la posición y el valor, añade dicho
    valor al en la posición que se envía como parametro.
2. append: Añade un valor al final del arreglo
'''
#Ejempl con isert
print('\n Añadimos el valor 200 en el indice 0, en el arreglo "a" con insert : \n');
a = np.insert(a,0,200);
print(a);

#Ejemplo con append
print('\n Añadimos el valor 400 al final del arreglo "a" con append : \n');
a = np.append(a,400);
print(a);

'''
Para eliminar elementos del arreglo usamos delete
'''
#Ejemplo de delete
print('\n Eliminenmos el ultimo valor agregar al arreglo con delete: \n');
a = np.delete(a,-1);
print(a);

print('\n Elementos del arreglo: ', a.size);
print('\n Redimencionando el arreglo de 10 a 5 elementos \n');
a = np.resize(a,5);
print(a);

'''
Para concatener arreglos a partir de 2 arreglos
'''
print('Creamos un arreglo "a" de dimención 10, con numeros aleatorios de 0 al 10: ');
a = np.random.randint(0,10,10);
print(a);

print('Creamos un arreglo "b" de dimención 10, con numeros aleatorios de 0 al 10: ');
b = np.random.randint(0,10,10);
print(b);

print('\n Concatenando los arreglos "a" y "b" \n');
c = np.concatenate([a,b]);
print(c);
