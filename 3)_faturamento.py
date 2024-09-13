import json

def carregar_dados_faturamento(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def calcular_faturamento(dados_faturamento):
    faturamento_valido = [dia['valor'] for dia in dados_faturamento if dia['valor'] > 0]

    if len(faturamento_valido) == 0:
        print("Nenhum dia com faturamento válido foi encontrado.")
        return
    
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

    dias_acima_da_media = len([dia for dia in faturamento_valido if dia > media_faturamento])

    return menor_faturamento, maior_faturamento, dias_acima_da_media

caminho_arquivo = '3)_faturamento.json'

dados_faturamento = carregar_dados_faturamento(caminho_arquivo)

menor, maior, dias_acima_media = calcular_faturamento(dados_faturamento)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
