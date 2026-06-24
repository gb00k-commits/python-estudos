linha_teste = [1, 4, 5, 4, 1, 3,]
numeros_vistos = set()

# Criamos uma variavel para guardar o resultado
primeiro_duplicado = None

for numero in linha_teste:
    if numero in numeros_vistos:
        break
    # ADICIONE ESTA LINHA ABAIXO (alinhada com o IF):
    numeros_vistos.add(numero)

# COLOQUE O PRINT NO COMEÇO DA LINHA (fora do for):
print("Primeiro duplicado:", primeiro_duplicado)