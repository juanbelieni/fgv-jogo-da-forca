"""
       __                         __         ______                     
      / /___  ____ _____     ____/ /___ _   / ____/___  ______________ _
 __  / / __ \/ __ `/ __ \   / __  / __ `/  / /_  / __ \/ ___/ ___/ __ `/
/ /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / __/ / /_/ / /  / /__/ /_/ / 
\____/\____/\__, /\____/   \__,_/\__,_/  /_/    \____/_/   \___/\__,_/  
           /____/     

Grupo: Juan, Lucas, Yasmin, Nicole e Carlos
"""

from logica import escolher_palavra, revelar_letras, esconder_palavra

jogar = int(input("Você quer jogar forca? Insira 1 para jogar ou 0 para sair: "))

if(jogar == 1):
  print("Você tem 6 chances para acertar!")

else:
  print("Então deixa para próxima! Até mais :)")


while(jogar == 1):

  palavra_secreta = escolher_palavra()
  palavra_escondida = esconder_palavra(palavra_secreta)

  tentativas = 6

  while(tentativas != 0):
   
    letra = str(input("\nInsira uma letra: "))

    auxiliador = palavra_escondida
    palavra_escondida = revelar_letras(palavra_escondida, palavra_secreta, tentativas, letra)
    print(palavra_escondida)

    if(auxiliador == palavra_escondida):
      tentativas -= 1

    if "_" not in palavra_escondida:
      print("\nVocê ganhou! \°/")
      break;

    if tentativas <= 0:
      print(f"\nVocê perdeu! A palavra era {palavra_secreta}.")

  jogar = int(input("\nDeseja jogar novamente? Insira 1 para jogar ou 0 para sair: "))
  if(jogar == 0):
    print("Então deixa para próxima! Até mais :)")