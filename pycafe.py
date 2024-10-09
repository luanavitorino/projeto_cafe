import pandas as pd
import statistics
df = pd.read_excel('cafepython.xlsx')
idade = df['Idade:']
genero = df['Gênero:']
cosumo_Cafe = df['Você consome café? Se sim, prefere-o puro ou com leite?']
condicao_Consumo_Cafe = df['Você possui labirintite ou alguma condição que o impeça de consumir café?']
diabetes_Cafe = df['Você tem diabetes ou alguma condição que impeça o consumo de café com açúcar?']
xicaras_Cafe = df['Quantas xícaras de café você consome por dia?']
adocar_Cafe = df['Qual sua forma de adoçar favorita?']
impedimento_consumo_cafe = df['Se você é cardiopata e/ou frequenta a academia, isso impede o consumo de café, considerando que os suplementos que utiliza já contém cafeína?']

#statistics
media_idade = statistics.mean(idade)
mediana_idade = statistics.median(idade)
try:
    moda_idade = statistics.mode(idade)
except statistics.StatisticsError:
    moda_idade = "Nenhuma moda encontrada"

print(f"Média de Idade: {media_idade}")
print(f"Mediana de Idade: {mediana_idade}")
print(f"Moda de Idade: {moda_idade}")
