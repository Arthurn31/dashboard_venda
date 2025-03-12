import json
import random
from datetime import datetime, timedelta

def gerar_dados_vendas_sem_acentos(num_linhas=5000):
    """Gera um arquivo JSON com dados de vendas aleatórios em UTF-8, sem acentos e caracteres especiais nas colunas."""

    produtos = ["Smartphone", "Notebook", "Tablet", "Fone de ouvido", "Camera", "Livro", "Jogo", "Roupa", "Sapato", "Acessorio"]
    categorias = ["Eletronicos", "Livros", "Jogos", "Moda"]
    vendedores = ["Joao Silva", "Maria Oliveira", "Pedro Santos", "Ana Souza", "Lucas Pereira"]
    ufs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    tipos_pagamento = ["cartao_credito", "boleto", "pix"]

    dados = []
    data_inicio = datetime(2020, 1, 1)  # Data de início: 1 de janeiro de 2020
    data_fim = datetime.now()  # Data de fim: data atual

    for _ in range(num_linhas):
        produto = random.choice(produtos)
        categoria = random.choice(categorias)
        preco = round(random.uniform(1000, 10000), 2)
        frete = round(random.uniform(10, 50), 2)

        # Gera uma data aleatória entre 2020 e hoje
        tempo_decorrido = data_fim - data_inicio
        dias_aleatorios = random.randint(0, tempo_decorrido.days)
        data_compra = (data_inicio + timedelta(days=dias_aleatorios)).strftime("%d/%m/%Y")

        vendedor = random.choice(vendedores)
        local_compra = random.choice(ufs)
        avaliacao = random.randint(1, 5)
        tipo_pagamento = random.choice(tipos_pagamento)
        parcelas = random.randint(1, 12) if tipo_pagamento == "cartao_credito" else 1
        lat = round(random.uniform(-34.0, 5.0), 2)
        lon = round(random.uniform(-74.0, -34.0), 2)

        dados.append({
            "Produto": produto,
            "Categoria_do_Produto": categoria,
            "Preco": preco,
            "Frete": frete,
            "Data_da_Compra": data_compra,
            "Vendedor": vendedor,
            "Local_da_compra": local_compra,
            "Avaliacao_da_compra": avaliacao,
            "Tipo_de_pagamento": tipo_pagamento,
            "Quantidade_de_parcelas": parcelas,
            "lat": lat,
            "lon": lon
        })

    with open("vendas_sem_acentos.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    gerar_dados_vendas_sem_acentos()
    print("Arquivo vendas_sem_acentos.json gerado com sucesso em UTF-8, sem acentos e caracteres especiais nas colunas!")