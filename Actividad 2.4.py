import pandas as pd

df = pd.read_excel("Consumo Gasolina.xlsx")

print(df)
print(df["Modelo"].mean())
print(df["Potencia (HP)"].max())
print(df["R. Comb. (Km/l)"].min())
print(df["R. Comb. (Km/l)"].describe())
print(df[df["Modelo"]>2015])
df3cilindros = df[df["Cilindros"]]
print(df3cilindros)
