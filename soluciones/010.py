import pandas as pd

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Limpiar profesión
df['profesion'] = df['profesion'].astype(str)
df['profesion'] = df['profesion'].str.replace(r'[^a-zA-Z ]', '', regex=True)
df['profesion'] = df['profesion'].str.strip().str.title()

# Contar Programador
cantidad = df[df['profesion'] == 'Programador'].shape[0]

print(f"La profesión Programador aparece: {cantidad} registros después de limpiar")