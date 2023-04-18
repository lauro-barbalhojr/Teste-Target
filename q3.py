import json

# Importando os dados em json e armazenando em uma list
with open('dados.json') as dados_json:
    ganho_diario = json.load(dados_json)

# Variáveis inicializadas com o valor do primeiro dia
menor_valor = ganho_diario[0]['valor']
maior_valor = ganho_diario[0]['valor']
soma_valores = ganho_diario[0]['valor']
dias_acima_da_media = 0
dias_validos: int = 1

# Loop fazendo os dias
for dia in ganho_diario[1:]:
    #Atribuindo a variável valor ao atributo 'valor' da seção 'dia' da list
    valor = dia['valor']
    if valor > 0:
        # Encontrando o menor valor
        if valor < menor_valor:
            menor_valor = valor
        # Encontrando o maior valor
        if valor > maior_valor:
            maior_valor = valor
        # Somando os valores
        soma_valores += valor
        # Incrementando os dias
        dias_validos += 1
        # Calculando a média mensal dos valores
        media_mensal = soma_valores / dias_validos
        # Encontrando o número de dias acima da média
        if valor > media_mensal:
            dias_acima_da_media += 1

print(f"Menor valor de faturamento diário: R${menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R${maior_valor:.2f}")
print(f"Número de dias com valor acima da média mensal: {dias_acima_da_media}")