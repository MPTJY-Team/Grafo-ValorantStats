import os
import pandas as pd
from sqlalchemy import create_engine

# COnfig conexão com o banco de dados
user = 'root'
password = '43690'
host = 'localhost'
port = 3306
database = 'vavastats'
table_name = 'tbl_players'
csv_filename = 'tbl_players.csv'

# Cria a string de conexão
engine = create_engine(
    f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

# Diretório para salvar os arquivos csv
diretorio = "Arquivo CSV/Arquivo_transicao"
os.makedirs(diretorio, exist_ok=True)  # Cria o diretório se ele não existir

# Caminho arquivo CSV
csv_path = os.path.join(diretorio, csv_filename)

# Executa a query e salva os resultados em um dataframe
df = pd.read_sql(table_name, engine)

# Salva o dataframe
df.to_csv(csv_path, index=False)

# Desliga conexão com o banco
engine.dispose()
