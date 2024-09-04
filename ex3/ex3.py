"""
3° QUESTÃO
"""

import json

def analisa_faturamento(arquivo_json):
    #LENDO O ARQUIVO JSON
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)

    #FILTRANDO APENAS DIAS COM FATURAMENTO
    faturamento_diario = [item['faturamento'] for item in dados if item['faturamento'] > 0]

    if not faturamento_diario:
        return "Não há dados de faturamento para análise."

    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)

    dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

arquivo_json = 'ex3/dados.json'

#TESTANDO
menor, maior, dias_acima_da_media = analisa_faturamento(arquivo_json)
print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

