#variaveis
cont = 0
vet = [0]*10
impar = 0

#algoritmo
for cont in range(0,10,1):
    vet[cont] = int(input(f"Informe o número {cont}: "))

print(f"Os números localizados nas posições impares são: ")
for cont in range(1,10,2):
    print(f"[{vet[cont]}]", end=' ')