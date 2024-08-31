import json
from statistics import mean

def analyze_faturamento(data):
  
    faturamento = [dia['valor'] for dia in data if dia['valor'] > 0]
    
    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    
    media_mensal = mean(faturamento)
    dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_media

with open('faturamento.json', 'r') as file:
    data = json.load(file)

menor, maior, dias_acima = analyze_faturamento(data)

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Número de dias acima da média: {dias_acima}")
