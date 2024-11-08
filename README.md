# Case técnico - beAnalytic

Este repositório contém a solução do teste técnico da beAnalytic, que consiste em três etapas:

- **Extração dos dados**: Criei um script de webscraping que coleta os dados de vendas de jogos do site [SteamDB](https://steamdb.info/sales/). O script utiliza as bibliotecas Selenium para automação de navegação e extração dos dados e Pandas para manipulação e exportação dos dados;
- **Armazenamento no Google BigQuery** - Criação do dataset e tabela na cloud;
- **Visualização no Google Sheets** - Conexão do dataset no BigQuery com uma planilha no Google Sheets.
  
## Arquivos

- `scraping_steamdb.py`: Script principal de *scraping*, que coleta os dados e os salva em um arquivo CSV.
- `requirements.txt`: Lista de dependências do projeto para garantir a correta execução do script.
- `steamdb_sales.csv`: Arquivo CSV com os dados coletados.

## Tecnologias utilizadas
- Python
- Selenium
- Pandas
- Google BigQuery
- Google Sheets

## Uso do script

1. Instale as dependências com:
   ```bash
   pip install -r requirements.txt
    ```
2. Execute o script:
   ```bash
   python scraping_steamdb.py
   ```
O script gerará ou atualizará o arquivo steamdb_sales.csv com os dados coletados.

## Estrutura das tabelas no Google BigQuery e Transformações realizadas

1. Visualização da tabela bruta carregada a partir do arquivo csv extraído pelo scraping:
   
   ![raw_table_view](https://github.com/user-attachments/assets/868889cd-ed1e-4543-b219-d33716dbd426)

2. Criação da tabela 'cleaned' para receber as transformações. Nessa etapa, já foi realizada uma transformação preliminar nos nomes das colunas (para snake_case) e nos valores das colunas 'discount' e 'rating', para arredondar as casas decimais e facilitar a compreensão.

   ![create_cleaned_table](https://github.com/user-attachments/assets/b2ddb55e-b0dd-404d-a22d-b211913cb888)

3. Adição de duas novas colunas na tabela 'cleaned': 'release_month' e 'release_year', do tipo int64.

   ![add_month_and_year_columns](https://github.com/user-attachments/assets/5a444254-9dfd-4ba8-a878-453123c7c7dc)

4. Divisão da coluna 'release_date', do tipo string, para as duas colunas criadas no passo anterior, que receberam o valor do mês e ano de ano, respectivamente. O intuito dessa transformação é facilitar o uso posterior em uma análise.
   
![divide_data_column](https://github.com/user-attachments/assets/095dced4-62da-4edc-b213-236e0e551413)

5. Visualização da tabela transformada final.

   ![cleaned_table_view](https://github.com/user-attachments/assets/274cf091-2913-4307-93f6-bfa61fb98fdf)

## Conexão da tabela transformada com o Google Sheets

- Ao final do processo, a tabela com as transformações foi conectada a uma planilha no Google Sheets

  ![google_sheets_connected](https://github.com/user-attachments/assets/1a42715b-596f-494a-af97-e2efd49bd2c4)


## Melhorias futuras

- Automatização da extração: configurar uma Cloud Function ou um Cloud Scheduler para automatizar a execução do script de scraping e atualização dos dados no BigQuery.
- Integração com ferramentas de data visualization: configurar a conexão desse dataset com alguma ferramenta de visualização, como o Looker Studio, por exemplo, para gerar dashboards.
