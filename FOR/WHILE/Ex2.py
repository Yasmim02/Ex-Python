#variaveis
idade = 0
contador = 0
n = 0
idade_soma = 0
idade_maior = 0
idade_menor = 0
idade_media = 0.0

#programa
n = int(input("Qual o número de pessoas? "))

for contador in range(0,n,1):
    idade = int(input("Informe a idade da pessoa: "))
    
    if(contador == 0):
        idade_maior = idade
        idade_menor = idade
    else:
        if(idade > idade_maior):
            idade_maior = idade
      
        if(idade < idade_menor):
            idade_menor = idade
    
    idade_soma += idade
    #idade_soma = idade_soma + idade
    
idade_media = idade_soma / n

print(f"A idade média é: {idade_media:,.2f}")
print(f"A menor idade é: {idade_menor}")
print(f"A maior idade é: {idade_maior}")