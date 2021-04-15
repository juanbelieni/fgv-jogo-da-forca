"""
Módulo gráfico do jogo da forca fornecido por
Grupo: Juan, Lucas, Yasmin, Nicole e Carlos
"""
import os 

def abertura(): #Imprime uma abertura na tela inicial do game 

  print("""
  Do you wanna play a game? (não é jogos mortais - não pra você)\n
                ─────▄██▀▀▀▀▀▀▀▀▀▀▀▀▀██▄─────
                ────███───────────────███────
                ───███─────────────────███───
                ──███───▄▀▀▄─────▄▀▀▄───███──
                ─████─▄▀────▀▄─▄▀────▀▄─████─
                ─████──▄████─────████▄──█████
                █████─██▓▓▓██───██▓▓▓██─█████
                █████─██▓█▓██───██▓█▓██─█████
                █████─██▓▓▓█▀─▄─▀█▓▓▓██─█████
                ████▀──▀▀▀▀▀─▄█▄─▀▀▀▀▀──▀████
                ███─▄▀▀▀▄────███────▄▀▀▀▄─███
                ███──▄▀▄─█──█████──█─▄▀▄──███
                ███─█──█─█──█████──█─█──█─███
                ███─█─▀──█─▄█████▄─█──▀─█─███
                ███▄─▀▀▀▀──█─▀█▀─█──▀▀▀▀─▄███
                ████─────────────────────████
                ─███───▀█████████████▀───████
                ─███───────█─────█───────████
                ─████─────█───────█─────█████
                ───███▄──█────█────█──▄█████─
                ─────▀█████▄▄███▄▄█████▀─────
                ──────────█▄─────▄█──────────
                ──────────▄█─────█▄──────────
                ───────▄████─────████▄───────
                ─────▄███████───███████▄─────
                ───▄█████████████████████▄───
                ─▄███▀───███████████───▀███▄─
                ███▀─────███████████─────▀███
                ▌▌▌▌▒▒───███████████───▒▒▐▐▐▐
                ─────▒▒──███████████──▒▒─────
                ──────▒▒─███████████─▒▒──────
                ───────▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒───────
                ─────────████░░█████─────────
                ────────█████░░██████────────
                ──────███████░░███████───────
                ─────█████──█░░█──█████──────
                ─────█████──████──█████──────
                ──────████──████──████───────
                ──────████──████──████───────
                ──────████───██───████───────
                ──────████───██───████───────
                ──────████──████──████───────
                ─██────██───████───██─────██─
                ─██───████──████──████────██─
                ─███████████████████████████─
                ─██─────────████──────────██─
                ─██─────────████──────────██─
                ────────────████─────────────
                ─────────────██──────────────
    """)
  input("Digite enter para continuar...")

def printa_forca(tentativas): #imprime a forca
    # seguinte meus ursinhos carinhosos 
    # essa função plota a forca em razão de quantas tentativas ainda restam
    
  erros = 6 - tentativas

  forca = """        


      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▐        
      █                                    
      █                                     
      █                                     
      █                                 
      █                              
      █                              
      █                                  
      █                        
      █                                   
      █                                   
      █                                 
      █                                  
      █                                    
      █                                   
      █                                   
      █                                   
      █                                  
      █                             
      █                                               
      █      
      █                                      
▀▀▀▀▀▀▀▀▀▀▀▀▀                         
    """

  cabeca = """ 
  

      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▐        
      █                          |          
      █                          |           
      █                          |           
      █                        @@@@@@         
      █                       @@@@@@@@       
      █                        @@@@@@        
      █                                    
      █                        
      █                                   
      █                                   
      █                                 
      █                                  
      █                                    
      █                                   
      █                                   
      █                                   
      █                                  
      █                             
      █                                            
      █                                     
      █                                      
▀▀▀▀▀▀▀▀▀▀▀▀▀                         
    """                      

  tronco = """ 
                                                                
      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▐        
      █                          |          
      █                          |           
      █                          |           
      █                        @@@@@@         
      █                       @@@@@@@@       
      █                        @@@@@@        
      █                          @@          
      █                          @@     
      █                          @@          
      █                          @@          
      █                          @@          
      █                          @@          
      █                          @@          
      █                          @@          
      █                          @@          
      █                              
      █                                   
      █                              
      █                                               
      █                                      
      █                                      
▀▀▀▀▀▀▀▀▀▀▀▀▀                         
    """    

  braco_esquerdo = """
                                                                
      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▐        
      █                          |          
      █                          |           
      █                          |           
      █                        @@@@@@         
      █                       @@@@@@@@       
      █                        @@@@@@        
      █                          @@          
      █                          @@     
      █                        @;@@          
      █                       @  @@          
      █                      @   @@          
      █                     @    @@          
      █                          @@          
      █                          @@                  
      █                          @@          
      █                              
      █                                   
      █                              
      █                                              
      █                                      
      █                                      
▀▀▀▀▀▀▀▀▀▀▀▀▀                         
    """ 

  braco_direito = """ 
                                                                
      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▐        
      █                          |          
      █                          |           
      █                          |           
      █                        @@@@@@         
      █                       @@@@@@@@       
      █                        @@@@@@        
      █                          @@          
      █                          @@     
      █                        @;@@;@          
      █                       @  @@  @        
      █                      @   @@   @       
      █                     @    @@    @      
      █                          @@          
      █                          @@          
      █                          @@                  
      █                              
      █                                   
      █                              
      █                                               
      █                                  
      █                                      
▀▀▀▀▀▀▀▀▀▀▀▀▀                         
    """ 



  perna_esquerda = """ 
                                                                
      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▐        
      █                          |          
      █                          |           
      █                          |           
      █                        @@@@@@         
      █                       @@@@@@@@       
      █                        @@@@@@        
      █                          @@          
      █                          @@     
      █                        @;@@;@          
      █                       @  @@  @        
      █                      @   @@   @       
      █                     @    @@    @      
      █                          @@          
      █                          @@                   
      █                         @@@@          
      █                        @@     
      █                       @@           
      █                      @@       
      █                     @@                      
      █                                  
      █                                      
▀▀▀▀▀▀▀▀▀▀▀▀▀                         
    """   

  perna_direita = """ 
                                                        
      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▐        
      █                          |          
      █                          |           
      █                          |           
      █                        @@@@@@         
      █                       @ X  X @       
      █                        @@@@@@        
      █                          @@          
      █                          @@     
      █                        @;@@;@          
      █                       @  @@  @        
      █                      @   @@   @       
      █                     @    @@    @
      █                          @@ 
      █                          @@
      █                         @@@@          
      █                        @@  @@   
      █                       @@    @@       
      █                      @@      @@ 
      █                     @@        @@            
      █                                  
      █                                      
▀▀▀▀▀▀▀▀▀▀▀▀▀                         
    """      

  parte_corpo = [forca, cabeca, tronco, braco_esquerdo, braco_direito, perna_esquerda, perna_direita]

  if erros > 6:
    print("Erro: número de erros é maior que 6")

  print(parte_corpo[erros])

def revelar_letras(palavra_escondida, palavra_secreta, letra): #Retorna a palavra escondida com as letras reveladas
  i = 0
  while  (i < len(palavra_secreta)):
    if(palavra_secreta[i] == letra):
      palavra_escondida = palavra_escondida[:i] + letra + palavra_escondida[i + 1:]
    i += 1

  return palavra_escondida

def ganhou(palavra_secreta): #imprime quando ganhar
  print(""" Parabéns! Você conseguiu :)\n

  __   __ _____  _   _     _    _  _____  _   _ 
  \ \ / /|  _  || | | |   | |  | ||_   _|| \ | |
   \ V / | | | || | | |   | |  | |  | |  |  \| |
    \ /  | | | || | | |   | |/\| |  | |  | . ` |
    | |  \ \_/ /| |_| |   \  /\  / _| |_ | |\  |
    \_/   \___/  \___/     \/  \/  \___/ \_| \_/
    """)
  print(f"\nA palavra era {palavra_secreta}\n\n")

def perdeu(palavra_secreta): #imprime quando perder
  print("\nVocê matou o bonequinho")
  print("""
  __   _______ _   _   _     _____ _____ _____ 
  \ \ / /  _  | | | | | |   |  _  /  ___|  ___|
   \ V /| | | | | | | | |   | | | \ `--.| |__  
    \ / | | | | | | | | |   | | | |`--. \  __| 
    | | \ \_/ / |_| | | |___\ \_/ /\__/ / |___ 
    \_/  \___/ \___/  \_____/\___/\____/\____/ """)

  print(f"\nA palavra era {palavra_secreta}\n\n")

def limpa_tela(): #limpa a tela e imprime o titulo do jogo
  os.system("clear")
  print("""
  
   |  _  _  _    _| _    |` _  _ _ _ 
 |_| (_)(_|(_)  (_|(_|   | (_)| (_(_|
         _|                          
  """)

def printa_letras_inseridas(letras_inseridas): #imprime letras inseridas
  """
  aqui voce entra com uma lista cuja cada posição corresponde a uma lista inserida pelo usuário
  Dessa forma, 
  """

  quantidade_de_letras = len(letras_inseridas)

  print("Letras inseridas: ", end = '')

  for posicao in range(0, quantidade_de_letras):
    print(letras_inseridas[posicao], end = ", ")

  print("\n")
  
def printa_falso_acerto(): #pro caso em que o usuario acerta mas ja tinha entrado com aquela letra
  print("Bom... errado você não está. Mas essa letra já foi escolhida anteriormente e você perdeu essa tentativa :D")

def tela_final(): #tela de encerramento :)
  print("""
    Foi bom enquanto durou!

  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  ░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
  ░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░
  ░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░
  ░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░
  ░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░
  ░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░
  ░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░
  ░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░
  ░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░
  ░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░
  ░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░
  ░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

    nyan cat está orgulhoso com
    a sua perspicácia!
  """)
