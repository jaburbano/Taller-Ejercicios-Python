import pandas as pd

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Convertir fecha
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'], errors='coerce')

# Filtrar entre 1990 y 2000
cantidad = df[
    (df['fecha_nacimiento'] >= '1990-01-01') &
    (df['fecha_nacimiento'] <= '2000-12-31')
].shape[0]

print(f"La cantidad de personas nacidas entre 1990 y 2000 es: {cantidad}")