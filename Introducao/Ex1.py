#Algoritmo
pes = 0.0
pol = 0.0
jardas = 0.0
milhas = 0.0

#programa

pes = float(input("Informe um valor em pes: "))

pol = pes * 12
jardas = (pes / 3)
milhas = (jardas / 1760)

print(f"Os valores convertidos são, {pol} polegadas, {jardas: ,.2f} jardas e {milhas: ,.2f} milhas. ")
