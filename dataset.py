import json
import pandas as pd

file = open("dados/vendas.json")

data = json.load(file)

df = pd.DataFrame.from_dict(data)

print(df["Data_da_Compra"])

df["Data_da_Compra"] = pd.to_datetime(df["Data_da_Compra"], format="%d/%m/%Y")

file.close()