import pandas as pd

# Cargar dataset
df = pd.read_csv('data/personas.csv')

# Convertir a texto
df['salario'] = df['salario'].astype(str)

# Buscar caracteres no numéricos
cantidad = df[df['salario'].str.contains(r'[^0-9]', regex=True)].shape[0]

print(f"La cantidad de salarios con caracteres no numéricos es: {cantidad}")