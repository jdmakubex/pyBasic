import pandas as pd

'''
Ordenamiento
'''

print('\n Leemos los datos desde un CSV  \n');
df = pd.read_csv('./input/incompletos.csv', index_col='id');
print(df);

print('\n Limpiaremos los datos, eliminando las filas donde hay valores nulos \n');
df = df.dropna();
print(df);

print('\n Obtener el usuario más jóven del país de Canadá. \n');
uj = df [df['pais'] == 'Canada'].sort_values('edad').head(1);
print(uj);

print('\n Obtener los 5 usuarios mas viejos de Alemania. \n');
# en el metodo .sort_values hay que pasar el parametro ascending=False para apagar el ordenamiento descendente
uj = df [df['pais'] == 'Germany'].sort_values('edad',ascending=False).head(5);
print(uj);

