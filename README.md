# Case técnico - beAnalytic

Este repositório contém uma parte da solução do teste técnico da beAnalytic, que consiste em três etapas:

- **Extração dos dados**: Criei um script de webscraping que coleta os dados de vendas de jogos do site [SteamDB](https://steamdb.info/sales/). O script utiliza as bibliotecas Selenium para automação de navegação e extração dos dados e Pandas para manipulação e exportação dos dados;
- **Armazenamento no Google BigQuery** - Criação do dataset e tabela na cloud;
- **Visualização no Google Sheets** - Conexão do dataset no BigQuery com uma planilha no Google Sheets.
  
## Arquivos

- `scraping_steamdb.py`: Script principal de *scraping*, que coleta os dados e os salva em um arquivo CSV.
- `requirements.txt`: Lista de dependências do projeto para garantir a correta execução do script.
- `steamdb_sales.csv`: Arquivo CSV com os dados coletados.

## Uso

1. Instale as dependências com:
   ```bash
   pip install -r requirements.txt
    ```
2. Execute o script:
   ```bash
   python scraping_steamdb.py
   ```
O script gerará ou atualizará o arquivo steamdb_sales.csv com os dados coletados.
