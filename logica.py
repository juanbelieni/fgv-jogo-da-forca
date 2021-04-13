"""
Módulo lógico do jogo da forca
Grupo: Juan, Lucas, Yasmin, Nicole e Carlos
"""

import random

def esconder_palavra(palavra_secreta):
  '''Retorna um string de underline de mesmo tamanho da palavra secreta'''
  return("_" * len(palavra_secreta))

def revelar_letras(palavra_escondida, palavra_secreta, tentativas, letra):
  '''Retorna a palavra escondida com as letras reveladas'''
  i = 0
  acertos = 0
  auxiliador = palavra_escondida
  while  (i < len(palavra_secreta)):
    if(palavra_secreta[i] == letra):
      palavra_escondida = palavra_escondida[:i] + letra + palavra_escondida[i + 1:]
      acertos += 1
    i += 1
  if(acertos > 0):
    print(f"Parabéns! Você acertou {acertos} letra(s)!")
    if(auxiliador == palavra_escondida):
      print("Mas, pela falta de atenção na repetição das letras, perdeu uma chance S2")
      tentativas -= 1
      print(f"Agora você tem {tentativas} tentativas")
  else:
    print("Infelizmente, não houve acertos :(")
    tentativas -= 1
    print(f"Agora você tem {tentativas} chances")
  return palavra_escondida

def escolher_palavra():
  palavras = open("palavras.txt", "r")
  palavras = palavras.read().split('\n')
  palavra_secreta = random.choice(palavras)
  return palavra_secreta