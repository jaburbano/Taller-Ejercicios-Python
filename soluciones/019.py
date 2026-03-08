import pandas as pd

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Buscar fechas con formato incorrecto
cantidad = df[~df['fecha_nacimiento'].astype(str).str.match(r'^\d{4}-\d{2}-\d{2}$')].shape[0]

print(f"La cantidad de fechas con formato incorrecto es: {cantidad}")