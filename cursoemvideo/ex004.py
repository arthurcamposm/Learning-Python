x = input('Digite algo:')
print(type(x), f'Possui números? {x.isnumeric()} Possui letras? {x.isalpha()} Possui letra ou número? {x.isalnum()}')
print(f'Possui letras minúsculas? {x.islower()} Possui letras maiúsculas? {x.isupper()}')
