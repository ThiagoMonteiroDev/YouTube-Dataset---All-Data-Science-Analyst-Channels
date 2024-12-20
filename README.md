# YouTube-Dataset---All-Data-Science-Analyst-Channels

# Análise de Dados do YouTube  

Este projeto contém uma análise detalhada de dados relacionados a canais de Ciência de Dados no YouTube. A análise explora métricas como visualizações, curtidas, comentários e o crescimento dos canais ao longo do tempo. A partir dessa análise, geramos insights sobre tópicos mais populares e padrões de crescimento.  

## Estrutura do Projeto  
A estrutura do projeto é a seguinte:  

project_folder/
├── Youtube_dataset_all_dataScience_channels.csv # Conjunto de dados original
├── Youtube_dataset_cleaned.csv # Conjunto de dados limpo e tratado
├── views_by_topic.csv # Dados de visualizações por tópico para Power BI
├── channel_growth.csv # Crescimento de visualizações por canal
├── manipula_csv.py # Script de limpeza e manipulação de dados
├── Untitled.ipynb # Notebook principal de análise
├── Relatório de Análise de Dados.pdf # Relatório detalhado da análise
├── Dashbord.pbix # Arquivo do Power BI com visualizações e relatórios
├── requirements.txt # Dependências do projeto

markdown
Copiar código

## Descrição dos Arquivos  
- **Youtube_dataset_all_dataScience_channels.csv**:  
  Contém os dados originais extraídos de vídeos de canais de Ciência de Dados no YouTube, incluindo informações como visualizações, curtidas e comentários.  

- **Youtube_dataset_cleaned.csv**:  
  Dados tratados e limpos, prontos para análise. Inclui correções de inconsistências e preenchimento de valores ausentes.  

- **views_by_topic.csv**:  
  Dados sobre a quantidade de visualizações por tópico, útil para análises no Power BI.  

- **channel_growth.csv**:  
  Informações sobre o crescimento das visualizações de cada canal, comparando períodos distintos.  

- **manipula_csv.py**:  
  Script em Python que realiza a limpeza e pré-processamento do dataset original.  

- **Untitled.ipynb**:  
  Notebook que contém as etapas de pré-processamento, análise exploratória e geração de visualizações para insights detalhados.  

- **Relatório de Análise de Dados.pdf**:  
  Documento contendo uma análise detalhada das descobertas, gráficos e insights obtidos.  

- **Dashbord.pbix**:  
  Arquivo do Power BI contendo visualizações interativas e relatórios baseados nos dados tratados.  

- **requirements.txt**:  
  Lista todas as dependências necessárias para executar o projeto.  

## Como Usar  

### 1. Instalar Dependências  
Clone o repositório e instale as dependências necessárias utilizando o arquivo `requirements.txt`:  
```bash
git clone <link-do-repositorio>  
cd <diretorio-do-projeto>  
pip install -r requirements.txt  
2. Executar a Análise
A análise é realizada no notebook Untitled.ipynb. Abra e execute as células diretamente em um ambiente Jupyter Notebook ou JupyterLab:

bash
Copiar código
jupyter notebook Untitled.ipynb  
3. Gerar Relatórios
Após a execução do notebook ou script Python, os arquivos CSV (como Youtube_dataset_cleaned.csv, views_by_topic.csv, e channel_growth.csv) serão gerados. Esses arquivos podem ser usados para criar visualizações adicionais ou importados para o Power BI.

4. Explorar o Dashboard
Abra o arquivo Dashbord.pbix no Power BI Desktop para explorar as visualizações interativas e relatórios.

Dependências
As principais bibliotecas e ferramentas utilizadas incluem:

pandas: Para manipulação e análise de dados.
matplotlib e seaborn: Para visualização de dados.
jupyter: Para execução do notebook interativo.
Instale as dependências com:

bash
Copiar código
pip install -r requirements.txt  
Resultados Obtidos
Insights sobre tópicos populares: Identificação dos tópicos com maior engajamento, como Python e IA.
Padrões de crescimento: Análise de crescimento por canal ao longo do tempo.
Dashboard interativo: Visualizações no Power BI para explorar os dados com facilidade.
Autor(es)
