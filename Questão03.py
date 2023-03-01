import json

faturamentoJSON = '''
{
    "1": 0,
    "2": 500,
    "3": 150,
    "4": 450,
    "5": 100,
    "6": 450,
    "7": 150
}
'''

faturamento = json.loads(faturamentoJSON)

media = qtd = 0
menor = maior = None

for i in faturamento:
    fat = faturamento[i]
    
    if fat == 0:
        continue

    media += fat
    qtd += 1

    if maior is None:
        maior = i
        menor = i
        continue

    if fat < faturamento[menor]:
        menor = i
    
    if fat > faturamento[maior]:
        maior = i
    

print(f'''
A média de faturamento desse mês foi de R${media/qtd:.2f}
O maior faturamento foi no dia {maior} com R$ {faturamento[maior]}
O menor faturamento foi no dia {menor} com R$ {faturamento[menor]}
''')