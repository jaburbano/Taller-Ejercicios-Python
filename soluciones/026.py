import pandas as pd

df = pd.read_csv('data/personas.csv')

df['ciudad'] = df['ciudad'].astype(str).str.replace(r'[^a-zA-Z ]', '', regex=True)
df['ciudad'] = df['ciudad'].str.strip().str.title()

df['activo'] = df['activo'].astype(str).str.strip().str.lower()

df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'], errors='coerce')

cantidad = df[
    (df['ciudad'] == 'Barranquilla') &
    (df['activo'] == 'true') &
    (df['fecha_nacimiento'] > '1980-01-01')
].shape[0]

print(f"La cantidad de personas activas en Barranquilla nacidas después de 1980 es: {cantidad}")