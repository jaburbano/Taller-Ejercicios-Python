import pandas as pd

df = pd.read_csv('data/personas.csv')

# limpiar profesion
df['profesion'] = df['profesion'].astype(str)
df['profesion'] = df['profesion'].str.replace(r'[^a-zA-Z ]', '', regex=True)
df['profesion'] = df['profesion'].str.strip().str.title()

# eliminar profesiones raras
frecuencia = df['profesion'].value_counts()
df = df[df['profesion'].isin(frecuencia[frecuencia > 500].index)]

# limpiar salario
df['salario'] = df['salario'].astype(str)
df['salario'] = df['salario'].str.replace(r'[^0-9]', '', regex=True)
df['salario'] = pd.to_numeric(df['salario'], errors='coerce')

# calcular promedio
promedio = df.groupby('profesion')['salario'].mean()

profesion = promedio.idxmax()

print(f"La profesión con el salario promedio más alto es: {profesion}")