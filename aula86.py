# Dictionary Comprehension e Set comprehension
produto = {
    'nome': 'Caneta azul',
    'preco': 2.5,
    'categoria': 'Escritorio'   
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave == 'categoria'
}

#print(dc)

lista = [
    ('a', 'Valor a'),
    ('b', 'Valor a'),
    ('c', 'Valor a'),
]

#dc = {
#    chave: valor
#    for chave, valor in lista
#}

#print(dict(lista))
print(set(range(10)))