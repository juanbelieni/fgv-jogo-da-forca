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

Módulo lógico do jogo da forca.
"""

import random

def tem_acento(palavra):
  '''Verifica se uma palavra tem acento (ou qualquer outro caractere especial)'''
  alfabeto = "abcdefghijklmnopqrstuvwxyz"
  for letra in palavra:
    if letra not in alfabeto:
      return True
  
  return False

def escolher_palavra():
  '''Retorna uma palavra aleatória'''
  palavras = open("palavras.txt", "r")
  palavras = palavras.read().split('\n')

  palavras = [palavra for palavra in palavras if len(palavra) > 3 and not tem_acento(palavra)]

  palavra_secreta = random.choice(palavras)
  return palavra_secreta

def esconder_palavra(palavra_secreta):
  '''Retorna um string de underline de mesmo tamanho da palavra secreta'''
  return("_" * len(palavra_secreta))

def revelar_letras(palavra_escondida, palavra_secreta, letra):
  '''Retorna a palavra escondida com as letras reveladas'''
  i = 0
  possui_letra = 0
  while  (i < len(palavra_secreta)):
    if(palavra_secreta[i] == letra):
      palavra_escondida = palavra_escondida[:i] + letra + palavra_escondida[i + 1:]
      possui_letra += 1
    i += 1

  return palavra_escondida

