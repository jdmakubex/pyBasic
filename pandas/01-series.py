import pandas as pd

'''
Las series, son una estructura de datos, propias de panda, de una sola dimención.
Los objetos de tipo series, poseen 2 arreglos.
Arreglo 1. Almacena los valores de la serie. 
Arreglo 2. Almacena los índices de la serie.
'''

print('Creamos una serie del 2 al 5 \n');
s = pd.Series([1,2,3,4,5,]);
print(s);

print('\n Comprobemos el tipo de de dato :',type(s));
print('\n Comprobemos la dimención de la serie :',s.size);
print('\n Comprobemos el tipo de dato almacensado en la serie :',s.dtype);
print('\n Conocer la forma de la serie :',s.shape);
print('\n Conocer los índices :',s.index);

print('\n Veamos el valor de la posición 5 de la serie :',s[4]);
print('\n Asignar  el valor  500 a la posición 5 la serie :');
s[4]=500;
print(s);

print('\n Creamos una nueva serie, con indices pesonalizados :');
serie = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'],name='úmeros',dtype=int);
#Otros dtype que se pueden declarar son: float, bool,str. etc.
print(serie);

print('\n Cambiamos el valor de que se almacena en la posición "a" :');
serie['a'] = 10;
print(serie);

'''
Otra forma es declarar diccionarios, en el cual, declaramos los valores pero también 
los índices de forma personalizada
'''

print('\n Creamos un diccionario :');
diccionario = {
'rojo' : 100,
'verde' : 200,
'azul' : 300,
'negro' : 400
}

print(diccionario)
print('\n Para crear una serie a partir de un diccionario');
ser = pd.Series(diccionario);
print(ser);