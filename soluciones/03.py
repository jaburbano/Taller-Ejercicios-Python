import pandas as pd
import codecs

df = pd.read_csv('data/personas.csv')

df['nombre'] = df['nombre_cifrado'].apply(lambda x: codecs.decode(str(x), 'rot_13'))
df['nombre'] = df['nombre'].str.strip().str.title()

cantidad = df[df['nombre'] == 'Juan'].shape[0]

print(f"El nombre Juan aparece: {cantidad} veces")