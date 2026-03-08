import pandas as pd

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Convertir id a texto
df['id'] = df['id'].astype(str)

# Buscar ids con caracteres no numéricos
cantidad = df[~df['id'].str.match(r'^\d+$')].shape[0]

print(f"el campo id con caracteres no numéricos tiene {cantidad} filas")