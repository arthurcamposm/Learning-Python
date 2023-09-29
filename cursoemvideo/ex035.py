r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\033[0;32mPode se formar um triângulo")
    if r1 == r2 == r3:
        print("\033[1;34mEsse triângulo é equilátero")
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print("\033[1;35mEsse triângulo é isósceles")
    else:
        print("\033[1;36m1Esse triângulo é escaleno")
else:
    print("\033[0;31m Não se pode formar um triângulo")


