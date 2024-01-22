import pandas as pd
import deltalake
from duckdb import connect

class DeltaPandasHandler:
    def __init__(self):
        # Define o número máximo de linhas e colunas a serem exibidas como None
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)


    def read_csv(self, file_path, **kwargs):
        """
        Função para ler um arquivo CSV usando pandas.
        """
        return pd.read_csv(file_path, **kwargs)

    def register(self, table_name, dataframe):
        """
        Função para registrar um DataFrame Pandas como uma tabela Delta em DuckDB.
        """
        con = connect()
        con.register(table_name, dataframe)
        con.close()

    def sql(self, query):
        """
        Função para executar uma consulta SQL em DuckDB.
        """
        con = connect()
        result = con.execute(query).fetchdf()
        con.close()
        return result
    
    def write_deltalake(self,file_path:str, **kwargs ):
        deltalake.write_deltalake(table_or_uri=file_path, **kwargs)