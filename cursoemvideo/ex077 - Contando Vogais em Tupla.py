palavras = ('aprender', 'programar', 'linguagem', 'python', 'estudar', 'gratis', 'trabalhar', 'curso', 'praticar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='') 
    for letra in p:
        if letra in 'aeiou'.lower():
            print(letra, end=' ')      