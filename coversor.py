pesos = input("¿cuantos pesos mexicanos tienes?: ")
pesos = float(pesos)
valor_dolar = 19.90
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")
