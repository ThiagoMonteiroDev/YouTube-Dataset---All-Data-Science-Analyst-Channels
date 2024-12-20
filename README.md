# Análise de Dados do YouTube

Este projeto realiza uma análise detalhada de dados relacionados a canais de Ciência de Dados no YouTube. A análise abrange métricas como visualizações, curtidas, comentários e o crescimento dos canais ao longo do tempo. O objetivo é identificar tópicos populares, padrões de engajamento e fornecer insights valiosos para a comunidade de dados.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

project_folder/ ├── Youtube_dataset_all_dataScience_channels.csv # Conjunto de dados original ├── Youtube_dataset_cleaned.csv # Conjunto de dados tratado e limpo ├── manipula_csv.py # Script para limpeza e manipulação de dados ├── Untitled.ipynb # Notebook principal de análise ├── Relatório de Análise de Dados.pdf # Relatório detalhado da análise ├── Dashbord.pbix # Dashboard interativo no Power BI ├── requirements.txt # Lista de dependências do projeto

php
Copiar código

## Descrição dos Arquivos

### Arquivos de Dados
- **Youtube_dataset_all_dataScience_channels.csv**:  
  Contém os dados brutos extraídos de canais de Ciência de Dados no YouTube. Inclui informações como visualizações, curtidas, comentários e outros dados relevantes.

- **Youtube_dataset_cleaned.csv**:  
  Arquivo gerado após o processo de limpeza e tratamento de dados. Ele contém informações organizadas, consistentes e prontas para análise.

### Scripts e Notebooks
- **manipula_csv.py**:  
  Script em Python responsável pela limpeza e manipulação do dataset original. Inclui etapas como remoção de valores inconsistentes, preenchimento de valores ausentes e padronização.

- **Untitled.ipynb**:  
  Notebook Jupyter contendo todas as etapas de análise de dados. Inclui:
  - Pré-processamento do dataset.
  - Análise exploratória com gráficos e estatísticas descritivas.
  - Geração de arquivos para visualizações no Power BI.

### Relatório e Visualizações
- **Relatório de Análise de Dados.pdf**:  
  Documento detalhado com explicações sobre as etapas de análise, gráficos gerados no notebook e os insights mais importantes.

- **Dashbord.pbix**:  
  Arquivo do Power BI contendo visualizações interativas baseadas nos dados tratados. Este arquivo permite explorar métricas como crescimento de canais, tópicos populares e engajamento.

### Outros Arquivos
- **requirements.txt**:  
  Lista de dependências do projeto. Inclui bibliotecas necessárias para rodar o notebook e scripts Python.

## Como Usar


### 1. Instalar Dependências
Clone o repositório e instale as dependências utilizando o arquivo requirements.txt:
bash 
git clone <link-do-repositorio>
cd <diretorio-do-projeto>
pip install -r requirements.txt

2. Executar o Notebook
Para realizar a análise, abra o notebook Untitled.ipynb em um ambiente Jupyter Notebook ou JupyterLab e execute as células:
jupyter notebook Untitled.ipynb

3. Gerar e Explorar Visualizações
Arquivos CSV Gerados:
Após a execução do notebook ou do script, os arquivos Youtube_dataset_cleaned.csv e outros processados serão gerados. Eles podem ser usados diretamente em ferramentas como Power BI.

Dashboard no Power BI:
Abra o arquivo Dashbord.pbix no Power BI Desktop para explorar as visualizações interativas.

Resultados Obtidos
Limpeza de Dados:
O arquivo Youtube_dataset_cleaned.csv contém dados tratados, removendo inconsistências e valores ausentes.

Análise Exploratória:
Gráficos gerados no notebook incluem:

Distribuição de visualizações por canal.
Análise de tópicos mais populares.
Crescimento de engajamento ao longo do tempo.
Dashboard Interativo:
O arquivo Dashbord.pbix permite explorar os resultados de forma visual e dinâmica, facilitando a interpretação dos insights.

Tecnologias Utilizadas
As ferramentas e bibliotecas utilizadas neste projeto incluem:

Python:
pandas: Manipulação e análise de dados.
matplotlib e seaborn: Visualizações gráficas.
jupyter: Execução de notebooks interativos.
Power BI: Criação de dashboards e relatórios interativos.
Ambientes:
Jupyter Notebook.
Power BI Desktop.

Com este projeto, é possível obter insights valiosos sobre o cenário de canais de Ciência de Dados no YouTube, identificando padrões e tendências que podem ser aplicados para melhorar estratégias de conteúdo e engajamento.

Copiar código
Se precisar de ajustes ou adicionar mais detalhes, posso ajudar! 😊

