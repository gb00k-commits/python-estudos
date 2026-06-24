carro = {
    'marca': 'Toyota',
    'modelo': 'Corolla',
    'ano': '2020',
    'cor': 'prata',
    'preco': '85000'
}

#dc = {}
#for chave, valor in carro.items():
    #if chave != 'preco':              
        #if isinstance(valor, str):    
            #dc[chave] = valor.upper()  
        #else:                         
            #dc[chave] = valor           

#print(dc)

dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in carro.items()
    if chave != 'preco'
}

print(dc)
