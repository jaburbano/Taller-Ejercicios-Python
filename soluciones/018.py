import pandas as pd

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Normalizar activo
df['activo'] = df['activo'].astype(str).str.strip().str.lower()

cantidad = df[df['activo'] == 'false'].shape[0]

print(f"La cantidad de registros inactivos (false) es: {cantidad}")