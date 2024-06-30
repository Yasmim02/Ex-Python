#algoritmo
nome = ""
situacao = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0 

#Progrma 
nome = input("Informe seu nome: ")
nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2? "))

media = (nota1 + nota2) / 2

if(media >= 6 ): 
    situacao = "Aprovado"
else:
    if(media >= 4) and (media < 6):
        situacao = "Recuperacao"
    else:
        situacao = "Reprovado"

print(f"{nome}, sua media e {media: ,.2} e sua situacao e {situacao}")