numero_str = input('vou dobrar o numero que vc digitar:'
)

try:
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f'o dobro de {numero_str} e {numero_float * 2:.2f}')
except:
    print('isso nao e um numero')
    
          