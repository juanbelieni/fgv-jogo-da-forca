"""
       __                         __         ______                     
      / /___  ____ _____     ____/ /___ _   / ____/___  ______________ _
 __  / / __ \/ __ `/ __ \   / __  / __ `/  / /_  / __ \/ ___/ ___/ __ `/
/ /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / __/ / /_/ / /  / /__/ /_/ / 
\____/\____/\__, /\____/   \__,_/\__,_/  /_/    \____/_/   \___/\__,_/  
           /____/     

Grupo: Juan, Lucas, Yasmin, Nicole e Carlos
"""

from logica import escolher_palavra, esconder_palavra, revelar_letras

from grafico import abertura, printa_forca, ganhou, perdeu, limpa_tela, tela_final

limpa_tela()
abertura()
limpa_tela()

while True:
    palavra_secreta = escolher_palavra()
    palavra_escondida = esconder_palavra(palavra_secreta)

    tentativas = 6


    while (tentativas != 0):
        limpa_tela()
        printa_forca(tentativas)
        print(palavra_escondida)

        letra = input("\nInsira uma letra: ")
        limpa_tela()
        auxiliador = palavra_escondida
        palavra_escondida = revelar_letras(palavra_escondida, palavra_secreta, letra)

        if (auxiliador == palavra_escondida):
            tentativas -= 1

        if "_" not in palavra_escondida:
            limpa_tela()
            ganhou(palavra_secreta)
            #input("Digite enter para continuar...")
            break

        if tentativas <= 0:
          printa_forca(tentativas)
          perdeu(palavra_secreta) 
          break

          #input("Digite enter para continuar...")

    continuar = input("Você quer continuar? Insira 1 para jogar ou 0 para sair: ")

    if continuar != "1" :
      limpa_tela() 
      tela_final()
      #input("Digite enter para continuar...")
      break
