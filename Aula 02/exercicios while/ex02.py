num = int(input("Digite um numero par: "))

while num % 2 != 0:
    num = int(input("Tente novamente, digite um numero par: "))
else:
    print(f"O numero escolhido foi: {num}")