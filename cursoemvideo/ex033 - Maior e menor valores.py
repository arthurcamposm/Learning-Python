n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 > n2 > n3:
    print(f'{n1} é o maior número e {n3} é o menor número')
elif n1 > n3 > n2:
    print(f'{n1} é o maior número e {n2} é o menor número')
elif n2 > n1 > n3:
    print(f'{n2} é o maior número e {n3} é o menor número')
elif n2 > n3 > n1:
    print(f'{n2} é o maior número e {n1} é o menor número')
elif n3 > n1 > n2:
    print(f'{n3} é o maior número e {n2} é o menor número')
else:
    print(f'{n3} é o maior número e {n1} é o menor número')
