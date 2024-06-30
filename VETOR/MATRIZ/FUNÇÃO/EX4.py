#variaveis
cont = 0
vet = [0.0]*5
vet2 = [0.0]*5


#algoritmo
for cont in range(0,5,1):
    vet[cont] = float(input(f"Informe o número {cont+1}: "))
    if(cont % 2 == 0 ):
        vet2[cont] = vet[cont] * 1.02
    else:
        vet2[cont] = vet[cont] * 1.05


for cont in range(0,5,1):
    print(f" {vet[cont]:.2f} ", end=' ')

print()
for cont in range(0,5,1):
    print(f" {vet2[cont]:.2f} ", end=' ')

