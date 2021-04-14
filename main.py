"""
       __                         __         ______                     
      / /___  ____ _____     ____/ /___ _   / ____/___  ______________ _
 __  / / __ \/ __ `/ __ \   / __  / __ `/  / /_  / __ \/ ___/ ___/ __ `/
/ /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / __/ / /_/ / /  / /__/ /_/ / 
\____/\____/\__, /\____/   \__,_/\__,_/  /_/    \____/_/   \___/\__,_/  
           /____/     

Grupo: Juan, Lucas, Yasmin, Nicole e Carlos
"""

from logica import escolher_palavra, revelar_letras, esconder_palavra, comecar_jogo
from grafico import printa_forca, abertura

abertura()
comecar_jogo()

while True:
  palavra_secreta = escolher_palavra()
  palavra_escondida = esconder_palavra(palavra_secreta)

  tentativas = 6

  while(tentativas != 0):
   
    letra = input("\nInsira uma letra: ")

    auxiliador = palavra_escondida
    palavra_escondida = revelar_letras(palavra_escondida, palavra_secreta, letra)
    print(palavra_secreta, palavra_escondida)

    if(auxiliador == palavra_escondida):
      tentativas -= 1

    printa_forca(tentativas)

    if "_" not in palavra_escondida:
      print("\nVocê ganhou! \°/")
      break;

    if tentativas <= 0:
      print(f"\nVocê perdeu! A palavra era {palavra_secreta}.")

  comecar_jogo()