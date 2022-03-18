dolares = input("¿cuantos dolares tines?: ")
dolares = float(dolares)
valor_pesos = 19.90
pesos = dolares * valor_pesos
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")