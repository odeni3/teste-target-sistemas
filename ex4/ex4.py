"""
4° QUESTÃO
"""

#DADOS
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

def calcular_percentuais(faturamento):
    total_faturamento = sum(faturamento.values())

    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}
    
    return percentuais

#TESTANDO
percentuais = calcular_percentuais(faturamento_estados)
print("Percentual de representação de faturamento por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
