"""
Módulo lógico do jogo da forca
Grupo: Juan, Lucas, Yasmin, Nicole e Carlos
"""

import random
import sys


def comecar_jogo():
  jogar = int(input("Você quer jogar forca? Insira 1 para jogar ou 0 para sair: "))

  if(jogar == 1):
    print("Você tem 6 chances para acertar!")
  else:
    print("Então deixa para próxima! Até mais :)")
    sys.exit()


def esconder_palavra(palavra_secreta):
  '''Retorna um string de underline de mesmo tamanho da palavra secreta'''
  return("_" * len(palavra_secreta))

def revelar_letras(palavra_escondida, palavra_secreta, letra):
  '''Retorna a palavra escondida com as letras reveladas'''
  i = 0
  while  (i < len(palavra_secreta)):
    if(palavra_secreta[i] == letra):
      palavra_escondida = palavra_escondida[:i] + letra + palavra_escondida[i + 1:]
    i += 1

  return palavra_escondida

def escolher_palavra():
  palavras = open("palavras.txt", "r")
  palavras = palavras.read().split('\n')
  palavra_secreta = random.choice(palavras)
  return palavra_secreta