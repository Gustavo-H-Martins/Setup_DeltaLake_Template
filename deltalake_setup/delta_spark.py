from multiprocessing import set_forkserver_preload
from pyspark.sql import SparkSession
from delta import *

class DeltaSparkHandler:
    def __init__(self) -> SparkSession:
        builder = SparkSession.builder.appName("SparkApp") \
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        
        self.spark = configure_spark_with_delta_pip(builder).getOrCreate()

    def read_csv(self, path:str, delimiter:str, encoding:str):
        """Faça a leitura de arquivos em diversos formatos, 
        com as devidas opções e passando o diretório do arquivo ou arquivos"""
        return self.spark.read.format("csv").option("delimiter", delimiter).option("encoding",encoding).load(path)

    def sql(self, query:str, **kwargs):
        """Faça consultas SQL no dataframe"""
        return self.spark.sql(query, **kwargs)
    
    def write_deltalake(self, dataframe ,file_path:str):
        """Faça a escrita de arquivos em diversos formatos,
        para Delta"""
        dataframe.write.format("delta").save(file_path)