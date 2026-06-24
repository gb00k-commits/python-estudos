# Generator exprension, iterables e iteratos em Python
#iterable = ['EU', 'Tenho', '__iter__']
#iterator = iter(iterable)

#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
import sys

iterable = ['EU', 'Tenho', '__iter__']
iterator = iter(iterable)
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

#for n in generator:
#   print(n)

print('varios numeros na memoria')