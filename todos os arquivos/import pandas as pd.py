import mysql.connector
import pandas as pd
import os

# Configurações de conexão com o banco de dados
config = {
    'user': 'root',
    'password': '43690',  # Senha atualizada conforme fornecido
    'host': 'localhost',
    'port': 3306,
    'database': 'mydb'  # Nome do banco de dados atualizado conforme fornecido
}

# Conexão com o banco de dados
con = mysql.connector.connect(**config)

# Diretório onde os arquivos CSV serão salvos
diretorio = "Arquivo CSV/Arquivo_transicao"

# Função para extrair dados de uma tabela e salvar em um arquivo CSV
def extrair_tabela(table_name, csv_filename):
    sql = f"SELECT * FROM {table_name}"  # Query SQL

    # Executa a query e armazena o resultado em um DataFrame
    df = pd.read_sql(sql, con)

    # Caminho completo do arquivo CSV
    csv_path = os.path.join(diretorio, csv_filename)
    
    # Salva o DataFrame em um arquivo CSV
    df.to_csv(csv_path, index=False)

# Cria o diretório se ele não existir
os.makedirs(diretorio, exist_ok=True)

# Chama a função para extrair os dados e salvar em um arquivo CSV
extrair_tabela("show_extract", "show_extract.csv")

# Fecha o cursor e a conexão com o banco de dados
con.close()
