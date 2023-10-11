expres = str(input('Digite uma expressão: '))

# Essas duas soluções abaixo não funcionam perfeitamente pois se os parênteses estiverem assim ") (" por exemplo, ainda vai resultar em uma expressão válida, quando na verdade esse exemplo não é uma expressão válida.

"""
lista1 = []
lista2 = []

if expres.count('(') == expres.count(')'):
    print('Expressão válida quanto ao uso do parênteses')
else:
    print('Expressão inválida quanto ao uso do parênteses')"""

"""for c in range(0, len(expres)):
    if expres[c] == '(':
        lista1.append(expres[c])
    elif expres[c] == ')':
        lista2.append(expres[c])
if len(lista1) == len(lista2):
    print('Expressão válida quanto ao uso do parênteses')
else:
    print('Expressão inválida quanto ao uso do parênteses')"""

# A solução abaixo funciona de forma mais completa
pilha = list()
for simb in expres:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida quanto ao uso do parênteses')
else:
    print('Expressão inválida quanto ao uso do parênteses')