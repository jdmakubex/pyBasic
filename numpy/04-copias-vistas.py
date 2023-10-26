'''
Copias: Son arreglos creados a partir de otro, 
        y contienen los mismos elementos del arreglo original. Si se hacen cambios en los
        elementos, cada objeto tiene cambios independientes

Vistas: La vista, apunta al arreglo original, si el objeto original tiene un cambio en sus elementos
        también se refleja en la vista, o si la vista tiene un cambio en sus elementos también se cambia
        en los elementos del arreglo original.
'''



import numpy as np

print('\n Creamos el arreglo original \n');
a = np.arange(0,10)
print (a);

print('\n Crear un a copia del arreglo a y almcenarlo en b \n');
b =  a.copy();
print (b);

print('\n comprobar si el arreglo a y el arreglo b son el mismo objeto \n');
print('ID del arreglo a: ',id(a));
print('ID del arreblo b: ',id(b));
print('¿el arreglo a es igual que el arreglo b? ', a is b);

print('\n Ahora creamos una vista almacenada en c, a partir de a  \n');
c = a.view()

print('\n comprobar si el arreglo a y el arreglo c son el mismo objeto \n');
print('ID del arreglo a: ',id(a));
print('ID del arreblo c: ',id(c));
print('¿el arreglo a es igual que el arreglo c? ', a is c);

print('\n Asigno el al ultimo elemento del arreglo a el valor 150 \n');
a[-1]=150
print('Elementos del vector a\n', a)
print('Elementos del vector c\n', c)
