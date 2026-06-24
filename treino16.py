pc = {
    'processador': 'Xeon E3',
    'placa_de_video': 'RX 580',
    'ram': '16gb'
}

pc['ram'] = '32gb'
pc['ssd'] = '480gb'

print(pc)

if 'ssd' in pc:
    print('O computador tem ssd!')
else:
    print('o computador nao tem ssd!')

print("\n--- CONGFIGURAÇÃO DO PC ---")
# O .items() entrega a chave e o valor ao mesmo tempo para o for
for chave, valor in pc.items():
    print(f"{chave.upper()}: {valor}")

          

