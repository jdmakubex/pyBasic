import numpy as np

'''Declaramos un arreglo con numpy y lo almacenamos en una variable'''
a = np.array([1,2,3,4,5])

'''Tipo de dato "a" '''
print(type(a))

'''Cantidad de elementos del arreglo'''
print(a.size)

'''Nos muestrea las dimenciones del arreglo'''
print(a.ndim)

'''Muestra el tipo de dato que se almacenó en el arreglo'''
print(a.dtype)

'''Conocer las dicmenciones de nuestro arreglo y los elementos de cada una de ellas'''
print(a.shape)

'''Suma 10 a cada elemento del arreglo'''
a = a+ 10
print(a)

'''Operaciones entre arreglos'''

b = np.array([6,7,8,9,10])

c = a + b

print(c)

'''Cambiando el tipado de los elementos de un arreglo'''
a = np.array([0,1,2,3,4,5],dtype=bool)
print(a)
a = np.array([0,1,2,3,4,5],dtype=np.complex64)
print(a)


'''Generar arreglos por ragos de numero'''
d = np.arange(0,30)
print(d)

'''Generar arreglo del 0 al 20 con saltos de 2 en 2'''
e = np.arange(0,20,2)
print(e)

'''Generar un arreglo de 10 ceros'''
z = np.zeros(10, dtype=int)
print(z)

'''Generar un arreglo de 10 unos'''
z = np.ones(10, dtype=int)
print(z)

'''Generar un arreglo vacío '''
em = np.empty(10, dtype=int)
print(em)

'''Generar un arreglo de 50 con numero aleatorios entre el 0 y el 100'''
al = np.random.randint(0,10,50)
print(al)



'''
En el siguiente ejemplo vamos a Obtener y actualizar elementos de un arreglo
'''

print('\n Genera un arreglo de 10 elementos, con numero aleatorios entre 0 y 10 \n');
a = np.random.randint(0,10,10);
print(a)

print('\n Obtenener el segundo elemento del arreglo de izquieda a derecha \n');
print(a[1]);

print('\n Obtenener el segundo elemento del arreglo de derecha a izquierda \n');
print(a[-2]);

print('\n Cambia el primer elemento por el valor 100 \n');
a[0]=100;
print(a);

