import pandas as pd

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Limpiar salario
df['salario'] = df['salario'].astype(str)
df['salario'] = df['salario'].str.replace(r'[^0-9]', '', regex=True)
df['salario'] = pd.to_numeric(df['salario'], errors='coerce')

# Obtener salario máximo
maximo = df['salario'].max()

print(f"El salario máximo después de limpiar es: {maximo}")