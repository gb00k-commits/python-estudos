nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print("Seu nome e", nome)
    print("seu nome invertido e", nome[::-1])
    print("Seu nome contem (ou nao) espaco:", ' 'in nome)
    print("Seu nome tem", len(nome),"Letras")
    print("A primeira letra do seu nome e", nome[0])
    print("A ultima letra do seu nome e", nome[-1])
if not nome or idade:
    print("Desculpe, voce deixou o campos vazos.")
