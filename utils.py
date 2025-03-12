
#importar base de dados
from dataset import df
import pandas as pd
import streamlit as st
import time

#Criando função para formatar números
def format_number(value, prefix=''):
    if value < 1000:
        return f'{prefix}{value:.0f}' 
    elif value < 1000000:
        return f'{prefix}{value / 1000:.2f} mil'
    else:
        return f'{prefix}{value / 1000000:.2f} milhões'
#fim da função  
#Receita por estado
def_rec_estado = df.groupby("Local_da_compra")[["Preco"]].sum()
def_rec_estado = df.drop_duplicates(subset=["Local_da_compra"])[["Local_da_compra","lat","lon"]].merge(def_rec_estado, left_on="Local_da_compra", right_index=True).sort_values(by="Preco", ascending=False)

#Receita Mesal
def_rec_mesal = df.set_index("Data_da_Compra").groupby(pd.Grouper(freq="ME"))[["Preco"]].sum().reset_index()
def_rec_mesal['Ano']=def_rec_mesal['Data_da_Compra'].dt.year
def_rec_mesal['Mes']=def_rec_mesal['Data_da_Compra'].dt.month_name()

# Receitas por categoria
def_rec_categoria = df.groupby("Categoria_do_Produto")[["Preco"]].sum().sort_values(by="Preco", ascending=False)
print(def_rec_categoria.head(5))
#Vendedores
def_vendedor = pd.DataFrame(df.groupby("Vendedor")["Preco"].agg(["sum","count"]))
#print(def_vendedor.head(5))
#funcao para coverter o arquvio csv

@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')
  
def mensagem_sucesso():
    success = st.success(
      'Arquivo CSV baixado com sucesso!',
      icon="✅")
    time.sleep(5)
    success.empty()

