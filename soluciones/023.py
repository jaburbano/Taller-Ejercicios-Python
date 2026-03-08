import pandas as pd
import codecs

df = pd.read_csv('data/personas.csv')

df['nombre'] = df['nombre_cifrado'].apply(lambda x: codecs.decode(str(x), 'rot_13'))
df['nombre'] = df['nombre'].str.strip().str.title()

df['ciudad'] = df['ciudad'].astype(str).str.replace(r'[^a-zA-Z ]', '', regex=True)
df['ciudad'] = df['ciudad'].str.strip().str.title()

cantidad = df[(df['nombre'] == 'Carlos') & (df['ciudad'] == 'Cali')].shape[0]

print(f"La cantidad de personas llamadas Carlos que viven en Cali es: {cantidad}")