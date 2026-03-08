import pandas as pd
import codecs

df = pd.read_csv('data/personas.csv')

df['nombre'] = df['nombre_cifrado'].apply(lambda x: codecs.decode(str(x), 'rot_13'))
df['nombre'] = df['nombre'].str.strip().str.title()

cantidad = df[df['nombre'] == 'Maria'].shape[0]

print(f"el nombre Maria aparece {cantidad}")