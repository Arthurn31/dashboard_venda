import streamlit as st
from dataset import df
from utils import convert_csv,mensagem_sucesso


st.title("Dataframe")
with st.expander("Dataset"):
    colunas = st.multiselect(
        "Selecione as colunas",
        list(df.columns),
        list(df.columns)
    )
st.sidebar.title("Filtros")
with st.sidebar.expander("Categoria do Produto"):
    filtro_categoria = st.multiselect(
        'Selecione as categorias',
        df["Categoria_do_Produto"].unique(),
        df["Categoria_do_Produto"].unique()
    )
with st.sidebar.expander("Preço do Produto"):
    filtro_preco = st.slider(
        "Selecione o Preco",
        df["Preco"].min(),
        df["Preco"].max(),
        (df["Preco"].min(), df["Preco"].max())
    )
with st.sidebar.expander("Data da Compra"):
    filtro_data = st.date_input(
        "Selecione a data",
        (df["Data_da_Compra"].min().date(), df["Data_da_Compra"].max().date())
    )

#query para usar os filtros
query = f'''
`Categoria_do_Produto` in @filtro_categoria and \
@filtro_preco[0] <= Preco and Preco <= @filtro_preco[1] and \
@filtro_data[0] <= `Data_da_Compra`.dt.date <= @filtro_data[1]
'''
filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]

st.dataframe(filtro_dados)

st.markdown(f'A Tabela possui:blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas')

#Baixar arquivo csv
st.markdown('Escreva  nome do arquivo')

coluna1,coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input(
      '',
      label_visibility='collapsed'
      )
    nome_arquivo += '.csv'
with coluna2:
  st.download_button(
    'Baixar arquivo',
    data = convert_csv(filtro_dados),
    file_name = nome_arquivo,
    mime = 'text/csv',
    on_click = mensagem_sucesso
  )
