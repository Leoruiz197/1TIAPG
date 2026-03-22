opcao = int(input("Digite de 1 a 7 para selecionar um dia da semana: "))

while True:
    match opcao:
        case 1 :
            print("Domingo")
            break
        case 2 :
            print("Segunda-Feira")
            break
        case 3 :
            print("Terça-Feira")
            break
        case 4 :
            print("Quarta-Feira")
            break
        case 5 :
            print("Quinta-Feira")
            break
        case 6 :
            print("Sexta-Feira")
            break
        case 7 :
            print("Sabado")
            break
        case _ :
            print("Opção invalida!")
            opcao = int(input("Digite de 1 a 7 para selecionar um dia da semana: "))