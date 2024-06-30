#variaveis
cont = 0
vet = [0]*4

#algoritmo
for cont in range(0,4,1):
    vet[cont] = int(input(f"Informe o número a para a posição {cont}: "))

for cont in range(4,0,-1):
    print(f"[{vet[cont]}]", end=' ')