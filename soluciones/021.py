import pandas as pd

df = pd.read_csv('data/personas.csv')

df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'], errors='coerce')

cantidad = df[df['fecha_nacimiento'] < '1960-01-01'].shape[0]

print(f"La cantidad de personas nacidas antes de 1960 es: {cantidad}")