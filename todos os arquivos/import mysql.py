import os
import pandas as pd
from sqlalchemy import create_engine

# Configurações de conexão com o banco de dados MySQL
user = 'root'
password = '43690'
host = 'localhost'
port = 3306
database = 'vavastats'
table_name = 'tbl_players'
csv_filename = 'tbl_players.csv'

# Cria a string de conexão SQLAlchemy
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

# Diretório onde os arquivos CSV serão salvos
diretorio = "Arquivo CSV/Arquivo_transicao"
os.makedirs(diretorio, exist_ok=True)  # Cria o diretório se ele não existir

# Caminho completo do arquivo CSV
csv_path = os.path.join(diretorio, csv_filename)

# Executa a query e armazena os resultados em um DataFrame usando a conexão SQLAlchemy
df = pd.read_sql(table_name, engine)

# Salva o DataFrame como um arquivo CSV
df.to_csv(csv_path, index=False)

# Fecha a conexão com o banco de dados
engine.dispose()
