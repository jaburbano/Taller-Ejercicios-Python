import pandas as pd

df = pd.read_csv('data/personas.csv')

cantidad = df[df['email'].astype(str).str.contains('@gmail.com', case=False, na=False)].shape[0]

print(f"La cantidad de correos con dominio gmail.com es: {cantidad}")