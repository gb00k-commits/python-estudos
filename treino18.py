compras = ["maca", "banana", "laranja", "maca", "melancia", "banana"]
compras_unicas = set(compras)

for fruta in compras_unicas:
    # Se a fruta atual for "maca", mostre uma mensagem especial
    if fruta == "maca":
        print('Achei a maca')
    else:
        print(fruta)