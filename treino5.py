numero = input("Digite um numero :")
numero = int(numero)

if numero % 2 == 0:
    print('Par')
else:
    print('impar')    

hora = input("Digite a hora: ")
hora = int(hora)

if hora < 0 or hora > 23:
    print("hora innvalida")

else:
    if hora <= 11:
        print('Bom dia')
    elif hora <= 17:
        print('boa tarde')
    else:
        print('boa noite')

nome = input("Digite seu nome: ")

if len (nome) <= 4:
    print("nome curto")

elif len (nome) <=6:
    print("nome normal")

else:
    print("nome muito grande")

