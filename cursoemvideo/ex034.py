sal = float(input("Qual é o seu salário? "))
if sal > 1250:
    nsal = sal + 10/100 * sal
else:
    nsal = sal + 15/100 * sal
print(f"O valor do salário com aumento é R${nsal:.2f}")
