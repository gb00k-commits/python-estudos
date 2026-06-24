import random

cinco_digitos = ''
for i in range(5):
    numero = random.randint(0, 9)
    cinco_digitos += str(numero)

print(cinco_digitos)