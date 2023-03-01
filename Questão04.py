dados ={"SP": 67836.43,
"RJ": 36678.66,
"MG": 29229.88,
"ES": 27165.48,
"Outros": 19849.53}

total = 0

for i in dados.values():
    total += i

print(f"O faturamento total mensal da empresa foi de R${total:.2f}\nSendo eles:")

for i in dados:
    print(f"{(dados[i]/total)*100:.1f}% em {i} com R$ {dados[i]}")