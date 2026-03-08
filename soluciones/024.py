import pandas as pd
import codecs

df = pd.read_csv('data/personas.csv')

df['nombre'] = df['nombre_cifrado'].apply(lambda x: codecs.decode(str(x), 'rot_13'))
df['nombre'] = df['nombre'].str.strip().str.title()

df['profesion'] = df['profesion'].astype(str).str.replace(r'[^a-zA-Z ]', '', regex=True)
df['profesion'] = df['profesion'].str.strip().str.title()

cantidad = df[(df['nombre'] == 'Ana') & (df['profesion'] == 'Medico')].shape[0]

print(f"La cantidad de personas llamadas Ana que son Medico es: {cantidad}")