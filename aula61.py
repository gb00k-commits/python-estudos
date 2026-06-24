cpf = '746824890'

soma = 0
contador = 10

for numero in cpf:
    soma += int(numero) * contador
    contador -= 1

resultado = (soma * 10) % 11

if resultado > 9:
    resultado = 0

print(resultado)