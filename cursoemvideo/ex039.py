from datetime import date
atual = date.today().year
ano = int(input('Digite o ano em que você nasceu: '))
idade = atual - ano
if idade < 18:
    print('Você ainda vai se alistar')
    x = 18 - idade
    print(f'Faltam {x} ano(s) para você se alistar')
elif idade == 18:
    print('Está na hora de se alistar')
elif idade > 18:
    print('Já passou da hora de se alistar')
    x = idade - 18
    print(f'Você passou {x} ano(s) do prazo do alistamento')
