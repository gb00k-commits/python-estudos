"""
closure e funcoes que retornam outras funcoes
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, [nome]!'
    return saudar()

falar_bom_dia = criar_saudacao('bom dia', 'Luiz')
falar_boa_noite = criar_saudacao('bom noite', 'Luiz')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

 
