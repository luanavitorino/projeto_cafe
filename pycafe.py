import pandas as pd
import statistics
import matplotlib.pyplot as plt

df = pd.read_csv('cafepython.csv', delimiter=';')

idade = pd.to_numeric(df['Idade:'], errors='coerce')

media_idade = statistics.mean(idade.dropna())
mediana_idade = statistics.median(idade.dropna())
try:
    moda_idade = statistics.mode(idade.dropna())
except statistics.StatisticsError:
    moda_idade = "Nenhuma moda encontrada"

def converter_xicaras(valor):
    if "1 - 2" in valor:
        return 1.5
    elif "3 - 4" in valor:
        return 3.5
    elif "5" in valor:
        return 5
    elif "De vez em quando" in valor or "Somente as vezes" in valor:
        return 0.5
    elif "Não consumo" in valor:
        return 0
    return None

xicaras_Cafe = df['Quantas xícaras de café você consome por dia?'].apply(converter_xicaras)

moda_genero = statistics.mode(df['Gênero:'])
moda_consumo_Cafe = statistics.mode(df['Você consome café? Se sim, prefere-o puro ou com leite?'])
moda_condicao_Consumo_Cafe = statistics.mode(df['Você possui labirintite ou alguma condição que o impeça de consumir café?'])
moda_diabetes_Cafe = statistics.mode(df['Você tem diabetes ou alguma condição que impeça o consumo de café com açúcar?'])
moda_adocar_Cafe = statistics.mode(df['Qual sua forma de adoçar favorita?'])
moda_impedimento_consumo_cafe = statistics.mode(df['Se você é cardiopata e/ou frequenta a academia, isso impede o consumo de café, considerando que os suplementos que utiliza já contém cafeína?'])

media_xicaras = statistics.mean(xicaras_Cafe.dropna())
mediana_xicaras = statistics.median(xicaras_Cafe.dropna())
try:
    moda_xicaras = statistics.mode(xicaras_Cafe.dropna())
except statistics.StatisticsError:
    moda_xicaras = "Nenhuma moda encontrada"

print(f"Média de Idade: {media_idade}")
print(f"Mediana de Idade: {mediana_idade}")
print(f"Moda de Idade: {moda_idade}")

print(f"Moda de Gênero: {moda_genero}")
print(f"Moda de Consumo de Café: {moda_consumo_Cafe}")
print(f"Moda de Condição para Consumo de Café: {moda_condicao_Consumo_Cafe}")
print(f"Moda de Diabetes (consumo de café): {moda_diabetes_Cafe}")
print(f"Moda de Forma de Adoçar: {moda_adocar_Cafe}")
print(f"Moda de Impedimento por Cardiopatia ou Academia: {moda_impedimento_consumo_cafe}")

print(f"\nMédia de Xícaras de Café por dia: {media_xicaras}")
print(f"Mediana de Xícaras de Café por dia: {mediana_xicaras}")
print(f"Moda de Xícaras de Café por dia: {moda_xicaras}")


genero_counts = df['Gênero:'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(genero_counts, labels=genero_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Gênero')
plt.show()


consumo_Cafe_counts = df['Você consome café? Se sim, prefere-o puro ou com leite?'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(consumo_Cafe_counts.index, consumo_Cafe_counts.values, color='teal')
plt.title('Preferências de Consumo de Café')
plt.xlabel('Tipo de Café')
plt.ylabel('Número de Pessoas')
plt.xticks(rotation=45)
plt.show()