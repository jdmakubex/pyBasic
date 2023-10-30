import pandas as pd
import numpy as np

'''
AUSENCIA DE VALORES
Se representa por "None", aunque tamién es común encontrearnos NaN, para gestionar esto
nos podemos apoyar de numpy mediante la constante nan:  np.nan
'''

print('Creamos una serie del 1 al 9 con valores nulos \n');
s = pd.Series([1,2,np.nan , np.nan, 5, 6, 7, np.nan, 9]);
print(s);

print('\n isnull para obtener valores ausentes :\n',s.isnull() );
print('\n notnull para obtener valores presentes : \n',s.notnull() );

print('\n conocer los indices con valores nulos :\n',s[s.isnull()] );
print('\n conocer los indices con valores presente :\n',s[s.notnull()] );

'''
Estas funciones: isnull() y s.notnull(), son útiles al momento de ejecutar una
limpieza de datos, para descartar valores nulos.
'''


