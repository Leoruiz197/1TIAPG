print("========= Menu =========")
print(" 1 - Ver Perfil")
print(" 2 - Editar Perfil")
print(" 3 - Sair")

opcao = int(input("Digite a opção correspondente: "))

while True:
    match opcao:
        case 1 :
            print("Ver perfil escolhido")
            break
        case 2 :
            print("Editar perfil escolhido")
            break
        case 3 :
            print("Saindo...")
            break
        case _ :
            print("Opção invalida!")
            opcao = int(input("Digite a opção correspondente: "))