nome = "Python"
metodo = "upper"

if hasattr(nome, metodo):
    print('Metodo encontrado')
    print(getattr(nome, metodo)())
else:
    print('Não existe o metodo')