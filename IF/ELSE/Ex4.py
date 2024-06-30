nome = ""
idade = 0

nome = (input("Informe seu nome: "))
idade = int(input("Informe a sua idade: "))

if(idade < 5 ):
    print("Não possui uma categoria válida!!")
elif(idade >= 5) and (idade <=7):
    print(f"{nome}, você tem {idade} anos, e sua classificação é Infantil A")
elif(idade >= 8) and (idade <= 11):
    print(f"{nome}, você tem {idade} anos, e sua classificação é Infantil B")
elif(idade >= 12) and (idade <= 13):
    print(f"{nome}, você tem {idade} anos, e sua classificação é Juvenil A")
elif(idade >= 13) and (idade <= 17):
    print(f"{nome}, você tem {idade} anos, e sua classificação é Juvenil B")
else: 
    print(f"{nome}, você tem {idade} anos, e sua Classificação é Adulto")