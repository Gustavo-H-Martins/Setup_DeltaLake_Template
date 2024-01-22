# 💾📀 DeltaLake Setup Inicial

Este projeto tem como objetivo fornecer um assistente para a configuração inicial do Delta Lake, permitindo a personalização das configurações de acordo com o caso de uso do usuário.

## 🗄👨‍💼👩‍💼 Conceitos

Um Data Lakehouse combina as características de um Data Lake e um Data Warehouse, permitindo a análise de dados em escala e a capacidade de operar com dados estruturados e semiestruturados. O Delta Lake é um componente essencial para a implementação de um Data Lakehouse, oferecendo confiabilidade transacional, escalabilidade e desempenho para cargas de trabalho de Big Data.

Dependendo do tamanho dos dados processados, é possível utilizar diferentes bibliotecas para o processamento, como Pandas, Polars ou Spark. Este projeto visa criar um módulo que, com base nos parâmetros fornecidos pelo usuário, instancia as configurações para leitura e processamento de diversos formatos de dados, utilizando Pandas, Polars ou Spark. Além disso, o resultado do processamento final será salvo como uma tabela Delta, independente da biblioteca utilizada para o processamento de dados.

## ♻🎣 Funcionalidades

- Configuração inicial personalizável para o Delta Lake
- Suporte para leitura e processamento de dados em diferentes formatos
- Integração com Pandas, Polars e Spark
- Salvamento do resultado do processamento como tabela Delta

## 🏁🏎 Como Utilizar

1. Clone o repositório
2. Execute o assistente de configuração inicial
3. Personalize as configurações conforme seu caso de uso
4. Realize o processamento de dados utilizando a biblioteca de sua escolha (Pandas, Polars ou Spark)
5. O resultado final será salvo como uma tabela Delta

## 🧑🏽 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 🧾 Licença

Este projeto está licenciado sob a [MIT License](./LICENSE).
