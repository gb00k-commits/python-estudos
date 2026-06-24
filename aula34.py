""""""
#repeticoes
#Executa uma acao enquanto uma condicao for verdadeira
#loop infinito -> quando um codigo nao tem fim
""""""
condicao = True

while condicao:
    nome = input('Digite seu nome')
    print(f'seu nome e {nome}')

    if nome == 'sair':
        break
