numeros = []
for i in range(15):
    numero = int(input("Introduce un número entero: "))
    numeros.append(numero)
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print("Los números pares introducidos son:")
for numero in pares:
    print(numero, end=" ,")
print()