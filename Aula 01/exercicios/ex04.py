distancia = float(input("Digite a distancia em Kms percorrida: "))
velMedia = float(input("Digite a velocidade média percorrida em Km/H: "))

resultado = distancia / velMedia
hora = int(resultado)
minuto = int((resultado - hora) * 60)

print(f"Tempo estimado de viagem é de: {hora}H:{minuto}m")