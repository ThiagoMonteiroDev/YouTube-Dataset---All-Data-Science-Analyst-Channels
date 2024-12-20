# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o conjunto de dados
file_path = "Youtube_dataset_all_dataScience_channels.csv"  # Altere para o caminho correto
df = pd.read_csv(file_path)

# Exibir as primeiras linhas do DataFrame
print("Primeiras linhas do arquivo CSV:")
print(df.head())

# Informações do DataFrame
print("\nInformações do DataFrame:")
print(df.info())

# Estatísticas básicas
print("\nEstatísticas básicas do DataFrame:")
print(df.describe())

# Verificar valores nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Tratar valores ausentes
df = df.dropna(subset=['Views', 'Like_count', 'Comment_Count'])  # Remover linhas com valores nulos em colunas críticas
print("\nValores nulos após tratamento:")
print(df.isnull().sum())

# Verificar duplicatas
print("\nNúmero de linhas duplicadas:", df.duplicated().sum())

# Remover duplicatas
df = df.drop_duplicates()
print("\nDuplicatas removidas. Número de linhas restantes:", len(df))



# Agrupar por canal e somar as visualizações
top_channels = df.groupby('Channel_Name')['Views'].sum().sort_values(ascending=False).head(10)

# Visualizar o resultado
plt.figure(figsize=(12, 6))
top_channels.plot(kind='bar', color='green')
plt.title("Top 10 Canais com Mais Visualizações")
plt.ylabel("Número de Visualizações")
plt.show()

# Matriz de correlação
correlation = df[['Views', 'Like_count', 'Comment_Count']].corr()



