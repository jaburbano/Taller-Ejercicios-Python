import pandas as pd

df = pd.read_csv('data/personas.csv')

df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'], errors='coerce')

fecha_actual = pd.to_datetime('2026-02-26')

edad = (fecha_actual - df['fecha_nacimiento']).dt.days / 365

cantidad = (edad > 50).sum()

print(f"La cantidad de personas con más de 50 años es: {cantidad}")