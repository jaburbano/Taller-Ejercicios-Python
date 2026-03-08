import pandas as pd

df = pd.read_csv('data/personas.csv')

df['ciudad'] = df['ciudad'].astype(str).str.replace(r'[^a-zA-Z ]', '', regex=True)
df['ciudad'] = df['ciudad'].str.strip().str.title()

df['profesion'] = df['profesion'].astype(str).str.replace(r'[^a-zA-Z ]', '', regex=True)
df['profesion'] = df['profesion'].str.strip().str.title()

ingenieros = df[df['profesion'] == 'Ingeniero']

ciudad = ingenieros['ciudad'].value_counts().idxmax()

print(f"La ciudad con más Ingenieros es: {ciudad}")