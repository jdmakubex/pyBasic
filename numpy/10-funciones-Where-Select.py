import numpy as np

print('Creamos un arreglo de 10 con calificaciones: ');
calificaciones = np.random.randint(1,11,10);
print(calificaciones);

print('\n Todas las calificaciones mayor o igual a 7 son aprobatorias: \n');

'''
Para condiciones siemples usamos el where
'''
r = np.where(calificaciones >= 7, 'Aprobaste','No aprobaste')
print(r);

'''
Para condiciones multiples, y con varios tipos de datos usamos el select
'''
#En este ejemplo agregamos mas condiciones, por lo que creamos un arreglo de condiciones
condiciones =  [
    (calificaciones == 10),
    ( (calificaciones == 8) | (calificaciones == 9) ),
    (calificaciones == 7),
    (calificaciones < 7)
];

#Generamos opciones que se van a mostrar conforme las condiciones
opciones = [
    'Felicidades, Aprobaste la masteria  con  10',
    'Felicidades, Aprobaste la masteria',
    'Aprobaste la masteria',
    'Lo sentimos, no aprobaste la materia'];

print('\n Utilizando un listado 4 condiciones: \n');
r2 = np.select(condiciones, opciones);
print(r2);
