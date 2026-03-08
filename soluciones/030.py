import pandas as pd
import codecs

df = pd.read_csv('data/personas.csv')

df['nombre'] = df['nombre_cifrado'].apply(lambda x: codecs.decode(str(x), 'rot_13'))
df['apellido'] = df['apellido_cifrado'].apply(lambda x: codecs.decode(str(x), 'rot_13'))

df['nombre'] = df['nombre'].str.strip().str.title()
df['apellido'] = df['apellido'].str.strip().str.title()

cantidad = df[(df['nombre'] == 'Jose') & (df['apellido'] == 'Garcia')].shape[0]

print(f"La cantidad de personas llamadas Jose Garcia es: {cantidad}")