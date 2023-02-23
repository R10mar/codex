lista= []
for lista in range(0,12):
    lista=int(input("dame un numero entero"))

numero=[]
for numero in range(0,12):
    numero=int(input("dame un numero de la lista"))
    while numero[lista] == lista:
        print("estoy dentro de la lista")
    if numero[lista] != lista:
            print("no estoy en la lista")   