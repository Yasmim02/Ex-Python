#algoritmo
carro = ""
tanque = 0.0
valor = 0.0
valorf = 0.0

#programa
print("Informe o tipo do seu carro:")
carro = (input("G - para Gasolina, ou A - para Alcool: "))
tanque = float(input("Informe a capacidade do seu tanque em litros: "))

if(carro == 'A'):
    print(f"Seu carro é a base de Alcool, e tem um tanque com capacidade de {tanque} litros.")
    valor = float(input("Informe o valor do Alcool: "))
else:
    print(f"Seu carro é a base de Gasolina, e tem um tanque com capacidade de {tanque} litros.")
    valor = float(input("Informe o valor da Gasolina: "))

valorf = (valor * tanque)

print(f"Para se encher o tanque é nescessario R$ {valorf}.")


