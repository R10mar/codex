gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0
print("1) Do you like Dawn or Dusk?:    ")
print ("1 si es Dawn")
print ("2 si es  Dusk")
respuesta1 = int(input("responde: "))
if respuesta1 == 1:
    gryffindor += 1
    ravenclaw  += 1
    print("ya veo.")
elif respuesta1 == 2 : 
    hufflepuff += 1
    slytherin += 1
    print("ya veo.")
else:
    print("eso no es una respuesta")
print("2) When Im dead, I want people to remember me as: ")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

respuesta2 = int(input("responde"))

if respuesta2 == 1:
    hufflepuff += 1
    print("ya veo.")
elif respuesta2 == 2:
    slytherin =+ 1
    print("ya veo.")
elif respuesta2 == 3:
    ravenclaw =+ 1
    print("ya veo.")
elif respuesta2 == 4 :
    gryffindor =+ 1
    print("ya veo.")
else:
    print("eso no es una respuesta")

print("3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
respuesta3 = int(input("responde"))

if respuesta3 == 1:
    slytherin += 1 
    print("ya veo.")
elif respuesta3 == 2 :
    hufflepuff += 1
    print("ya veo.")
elif respuesta3 == 3:
    ravenclaw += 1
    print("ya veo.")
elif respuesta3 == 4:
    gryffindor += 1
    print("ya veo.")
else:
    print("eso no una respusta)")


if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print(' Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('Ravenclaw!')
elif hufflepuff >= slytherin:
  print('Hufflepuff!')
else:
  print('Slytherin!')
