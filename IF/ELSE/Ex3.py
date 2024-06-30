#Algoritmo
amos = 0.0

#Programa

amos = int(input("Informe a quantidade de pontos de água na amostra: "))

if (amos <= 10):
    print("Classificação: Rochosa")
else:
    if(amos > 10) and (amos <= 40):
        print("Classificação: Firme")
    elif (amos > 40) and (amos <= 80):
        print("Classificação: Pantanosa")
    else: 
        print("Classificação Invalida!!!")