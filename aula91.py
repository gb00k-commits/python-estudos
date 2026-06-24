# introducão as Generatos Functions em Python
#generator = (n for n in range(1000000))

#def generator(n=0):
# yield 1 #pausa
#    print('Cntinuando...')
#    yield 2 #pausa
#    print('Mais uma vez...')
#    yield 3
#   print('Vou terminar')
#    return 'ACABOU'

# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)

