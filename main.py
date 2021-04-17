"""
       __                         __         ______                     
      / /___  ____ _____     ____/ /___ _   / ____/___  ______________ _
 __  / / __ \/ __ `/ __ \   / __  / __ `/  / /_  / __ \/ ___/ ___/ __ `/
/ /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / __/ / /_/ / /  / /__/ /_/ / 
\____/\____/\__, /\____/   \__,_/\__,_/  /_/    \____/_/   \___/\__,_/  
           /____/     

Grupo 7: 
Carlos Alberto de Souza Moreira Junior (B39056)
Juan Belieni de Castro Araujo (B43904)
Lucas Westfal (B43881)
Nicole dos Santos de Souza (B43888)
Yasmin Pádua Lugão (B44008)

Módulo principal do jogo da forca.
"""

from logica import escolher_palavra, esconder_palavra, revelar_letras

from grafico import inicio, forca, ganhou

while True:
  letras_certas = ""
  letras_erradas = ""

  palavra_secreta = escolher_palavra()
  palavra_escondida = esconder_palavra(palavra_secreta)

  tentativas = 6

  inicio()

  while (tentativas != 0):
    forca(6 - tentativas, letras_erradas, palavra_secreta)
    print(palavra_escondida)

    letra = input("\nInsira uma letra: ")[0]

    auxiliador = palavra_escondida
    palavra_escondida = revelar_letras(palavra_escondida, palavra_secreta, letra)

    if (auxiliador == palavra_escondida):
      tentativas -= 1
      if letra not in letras_erradas and letra not in letras_certas:
        letras_erradas += letra
    else:
      letras_certas += letra

    if "_" not in palavra_escondida:
      print()
      print(palavra_secreta)
      ganhou()
      break

    if tentativas <= 0:
      forca(6 - tentativas, letras_erradas, palavra_secreta)
      break

  continuar = input("Você quer continuar? Insira 1 para jogar ou 0 para sair: ")

  if continuar != "1" :
    break
