import random

tentativas = 2
num = 5
num = random.randint(1,10)

user_num = int(input("Digite um numero entre 1 - 10: "))
while user_num != num and tentativas > 0:
    print(f"Tentativas restantes: {tentativas}")
    user_num = int(input("Digite novamente um numero entre 1 - 10: "))
    tentativas -= 1

if user_num != num and tentativas == 0:
    print("Parabens vc definitivamente é um USUARIO!!!")
    print(f"O numero era {num}")
else:
    print("Parabens, vc foi promovido a PROGRAMADOR!")
    

