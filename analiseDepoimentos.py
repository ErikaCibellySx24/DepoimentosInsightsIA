import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

# Função para extrair dados dos relatórios
def extrair_dados(texto):
    tipo_crime = re.findall(r'(assalto|homicídio|furto|vandalismo|fraude)', texto, re.IGNORECASE)
    local = re.findall(r'na rua (.*?)(,|$)', texto)
    return tipo_crime[0] if tipo_crime else 'Desconhecido', local[0][0] if local else 'Desconhecido'

# Ler o arquivo de texto
with open('sentencas.txt', 'r', encoding='utf-8') as f:
    relatorios = f.readlines()

# Extrair dados e criar um DataFrame
dados = []
for relatorio in relatorios:
    tipo_crime, local = extrair_dados(relatorio)
    dados.append([tipo_crime, local])

df = pd.DataFrame(dados, columns=['Tipo de Crime', 'Local'])

# Análise de distribuição dos tipos de crimes
crime_counts = df['Tipo de Crime'].value_counts()

# 
plt.figure(figsize=(8, 6))
sns.barplot(x=crime_counts.index, y=crime_counts.values, palette='Blues_d')
plt.title('Distribuição dos Tipos de Crime')
plt.xlabel('Tipo de Crime')
plt.ylabel('Frequência')
plt.show()

# Análise de distribuição de locais
local_counts = df['Local'].value_counts()

# Estilizando o gráfico de locais de crime
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.barplot(x=local_counts.index, y=local_counts.values, palette='viridis', edgecolor='black')
plt.title('Distribuição dos Locais de Crime', fontsize=16, weight='bold')
plt.xlabel('Local', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
