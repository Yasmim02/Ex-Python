#Variaveis
linha = 0
coluna = 0
mat = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]

#algoritmo
for linha in range(0,5,1):
    for coluna in range(0,5,1):
        mat[linha][coluna] = int(input(f"Informe o número para a posição {linha} {coluna}: "))

for linha in range(0,5,1):
    for coluna in range(0,5,1):
        if(linha == coluna):
            print(f"[{mat[linha][coluna]}]", end=' ')
        else:
            print(f"[ ]", end=' ')
    print()
