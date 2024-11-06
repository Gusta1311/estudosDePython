#para importar uma biblioteca inteira
import math
#para importar algo especifico dessa biblioteca
from math import sqrt,trunc,ceil
#Se eu importar a biblioteca toda, para usar um comando tem que ser com math. Ex
math.sqrt(num)
#Se não eu posso so usar a função
sqrt(num)
#Tambem posso fazer algo a mais no print. Ex
from math import sqrt, ceil

num = float(input('Digite um número: '))
raiz = sqrt(num)

#importar randomização
import random

#importar especificamente alguns modulos do random
from random import randint,shuffle,choice#randint random com numeros inteiros, shuffle sorteia nomes ou numeros em uma ordem, choice sorteia um numero ou um nome

# Exibindo a raiz exata
print('A raiz exata de {} é {:.2f}'.format(num, raiz))

# Exibindo a raiz arredondada para cima
print('A raiz de {} arredondada para cima é {}'.format(num, ceil(raiz)))
#Ou ceil(raiz)/ceil serve para arredondar o numero para cima

