import pandas as pd

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Detectar espacios al inicio o final
cantidad = df[df['email'].astype(str).str.contains(r'^\s|\s$', regex=True)].shape[0]

print(f"La cantidad de emails con espacios adicionales es: {cantidad}")