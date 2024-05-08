import mysql.connector
import pandas as pd
import os

# Config conexão com o banco de dados
config = {
    'user': 'root',
    'password': '43690',
    'host': 'localhost',
    'port': 3306,
    'database': 'mydb'
}

# Conexão com o banco de dados
con = mysql.connector.connect(**config)

# Diretório para salvar os arquivos csv
diretorio = "Arquivo CSV/Arquivo_transicao"

# Função para extrair dados de uma tabela e salvar em um arquivo CSV


def extrair_tabela(table_name, csv_filename):
    sql = f"SELECT * FROM {table_name}"

    # Executa a query e salva os resultados em um dataframe
    df = pd.read_sql(sql, con)

    # Caminho arquivo CSV
    csv_path = os.path.join(diretorio, csv_filename)

    # Salva o dataframe
    df.to_csv(csv_path, index=False)


# Cria o diretório se ele não existir
os.makedirs(diretorio, exist_ok=True)

# Chama a função para extrair os dados e salvar em um arquivo CSV
extrair_tabela("show_extract", "show_extract.csv")

# Desliga conexão com o banco
con.close()
