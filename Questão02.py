fb1 = 0
fb2 = 1

entrada = int(input("Qual número deseja verificar?\n"))

while True:
    if entrada == fb1 or entrada <= fb2: 
        break

    novo = fb1 + fb2
    fb1, fb2 = fb2, novo

if entrada == fb1 or entrada == fb2:
    print("O número pertence a sequencia.")
else:
    print("O número não pertence a sequencia.")



