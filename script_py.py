# PROBLEMA 5.

import pandas as pd
import pyodbc

# Configurações do bancod de dados
DB_SERVER = 'DESKTOP-Server'
DB_NAME = 'Banco_de_dados'
DB_USER = 'user'
DB_PASSWORD = 'senha'
DRIVER = 'ODBC Driver 18 for SQL Server'

# Leitura do arquivo CSV
arquivo_csv = 'arquivo.csv'

df = pd.read_csv(arquivo_csv)

print(df)
print(f"Data types: ", df.dtypes.to_dict())

# Identificando os tipos de dados do data_frame

df_columns = df.columns.tolist()
df_columns2 = [col.replace(" ", "_") for col in df_columns]

df.columns = df_columns2
data_types = df.dtypes.to_dict()

type_mapping = {
    'object': 'VARCHAR(100)',
    'int64': 'BIGINT',
    'float64': 'FLOAT',
    'datetime[ns]': 'DATETIME',
    'bool': 'BIT'
}

columns_types = ", ".join(f"{col} {type_mapping[str(data_types[col])]}" for col in df.columns)


# Conexão com banco de dados usando pyodbc

#connection_str = f'DRIVER={DRIVER};SERVER={DB_SERVER};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD};Encrypt=no'
connection_str = f'DRIVER={DRIVER};SERVER={DB_SERVER};DATABASE={DB_NAME};TRUSTED_CONNECTION=yes;Encrypt=no'

connection = pyodbc.connect(connection_str)

# Criando tabela
cursor = connection.cursor()
cursor.execute(f'CREATE TABLE schema.TABELA_CSV ({columns_types});')

# Inserindo valores
values_list = [tuple(row) for row in df.values]
insert_str = f'INSERT INTO schema.TABELA_CSV ({", ".join(df.columns)}) VALUES ({", ".join(["?"] * len(df.columns))})'
cursor.executemany(insert_str, values_list)

connection.close()