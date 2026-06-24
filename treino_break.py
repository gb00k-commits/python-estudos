# uma lista de frutas simples e facil
frutas = ['maca', 'banana', 'morango', 'abacaxi', 'uva']

for fruta in frutas:
    print(f"Olhando a fruta {fruta}")

# Se a fruta for 'morango', o break vai parar o loop na hora!
    if fruta == 'morango':
        print("Achei o morango! parando loop ...")
        break   

print("o loop parou!")

