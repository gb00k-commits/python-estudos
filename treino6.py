palavra = "sozinho"
letras_digitadas = ""

while True:
    letra = input("Digite uma letra: ")
    letras_digitadas += letra     

    resultado = ""

    for i in palavra:
        if i in letras_digitadas:
            resultado += i
        else:
            resultado += '*'

        print(resultado)

    if resultado == palavra:
        print("Voce ganhou!")
        break
