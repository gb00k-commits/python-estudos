# Suas frutas favoritas
minhas_frutas = {"maca", "banana"}

# As frutas favorias do seu amigo
frutas_amigo = {"banana", "melancia"}

# 1. UNIÃO (|) -> Junta tudo e tira o que for repetido
todos_comem = minhas_frutas | frutas_amigo
print("União:", todos_comem)

# 2. INTERSECÇÃO (&) -> Mostra só o que os dois gostam igual
gostos_iguais = minhas_frutas & frutas_amigo
print("Intersecção:", gostos_iguais)
