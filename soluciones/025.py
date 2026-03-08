import pandas as pd

df = pd.read_csv('data/personas.csv')

df['profesion'] = df['profesion'].astype(str).str.replace(r'[^a-zA-Z ]', '', regex=True)
df['profesion'] = df['profesion'].str.strip().str.title()

df['salario'] = df['salario'].astype(str).str.replace(r'[^0-9]', '', regex=True)
df['salario'] = pd.to_numeric(df['salario'], errors='coerce')

cantidad = df[(df['profesion'] == 'Abogado') & (df['salario'] > 10000000)].shape[0]

print(f"La cantidad de Abogados con salario mayor a 10,000,000 es: {cantidad}")