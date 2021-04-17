# Membros do grupo:
'''
Bernardo Vargas (B37182);
Fernanda Durão (B43662);
João Pedro Menezes (B44431);
Maria Fernanda Machado (B43991);
Victor Caldas (B33012).
'''


# Para importar o módulo, armazene-o no mesmo diretório que o seu programa
# e escreva no seu código:

# from Bernardo_Fernanda_Joao_Maria_Victor.py import forca

# Parâmetros:
# quantidade_erros --> (int) quantidade de letras erradas que o jogador supôs
# letras_erradas --> (str) as letras que o jogador supôs errado
# resposta --> (str) a palavra secreta

# Desenha a forca de acordo com o número de erros do jogador 

def inicio():
    print('''
      __                                __             ___
     | |   ___     __ _    ___       __| |   __ _     / _|   ___    _ __    ___    __ _ 
  _  | |  / _ \   / _` |  / _ \     / _` |  / _` |   | |_   / _ \  | '__|  / __|  / _` |
 | |_| | | (_) | | (_| | | (_) |   | (_| | | (_| |   |  _| | (_) | | |    | (__  | (_| |
  \___/   \___/   \__, |  \___/     \__,_|  \__,_|   |_|    \___/  |_|     \___|  \__,_|
                  |___/                                                                                       
          ''')

def forca(quantidade_erros, letras_erradas, resposta): 
    cabeca = ""
    tronco = ""
    pernas = ""
    
    # Apenas desenha a forca vazia enquanto o jogador não erra
    if quantidade_erros == 0:
        print(f'''
          .___________.
          | ;_=_=_=_=_|{chr(9)*2}A resposta tem {len(resposta)} letras. 
          |||//{chr(9)} |
          |  /{chr(9)}{cabeca}
          | |{chr(9)}{tronco}{chr(9)*2}Você ainda não errou nenhuma.
          |||{chr(9)}{pernas}
          | |
          |||________,{chr(9)*2}Você tem 6 tentativas! 
          | _=_==_==_|
          |/        \|
          ''')
    
    
    # Adiciona a cabeça com 1 erro:
    elif quantidade_erros == 1:
        cabeca = "(_)"
        
        # Desenha a forca: 
        print(f'''
          .___________.
          | ;_=_=_=_=_|{chr(9)*2}A resposta tem {len(resposta)} letras. 
          |||//{chr(9)} |
          |  /{chr(9)}{cabeca}
          | |{chr(9)}{tronco}{chr(9)*2}Não tem a letra: {letras_erradas}
          |||{chr(9)}{pernas}
          | |
          |||________,{chr(9)*2}Continue! Ainda tem 5 tentativas! 
          | _=_==_==_|
          |/        \|
          ''')
        
    # Adiciona o tronco com 2 erros:
    elif quantidade_erros == 2:
        cabeca = "(_)"
        tronco = " | "
        
        # Desenha a forca: 
        print(f'''
          .___________.
          | ;_=_=_=_=_|{chr(9)*2}A resposta tem {len(resposta)} letras. 
          |||//{chr(9)} |
          |  /{chr(9)}{cabeca}
          | |{chr(9)}{tronco}{chr(9)*2}Não tem as letras: {letras_erradas}
          |||{chr(9)}{pernas}
          | |
          |||________,{chr(9)*2}Não desista! Ainda tem 4 tentativas! 
          | _=_==_==_|
          |/        \|
          ''')
        
        
    # Adiciona o braço esquerdo com 3 erros:
    elif quantidade_erros == 3:
        cabeca = "(_)"
        tronco = "/| "

        # Desenha a forca: 
        print(f'''
          .___________.
          | ;_=_=_=_=_|{chr(9)*2}A resposta tem {len(resposta)} letras. 
          |||//{chr(9)} |
          |  /{chr(9)}{cabeca}
          | |{chr(9)}{tronco}{chr(9)*2}Não tem as letras: {letras_erradas}
          |||{chr(9)}{pernas}
          | |
          |||________,{chr(9)*2}Você consegue! Ainda tem 3 tentativas! 
          | _=_==_==_|
          |/        \|
          ''')


        
    # Adiciona o braço direito com 4 erros:
    elif quantidade_erros == 4:
        cabeca = "(_)"
        tronco = "/|\ "
        
        # Desenha a forca: 
        print(f'''
          .___________.
          | ;_=_=_=_=_|{chr(9)*2}A resposta tem {len(resposta)} letras. 
          |||//{chr(9)} |
          |  /{chr(9)}{cabeca}
          |||{chr(9)}{tronco}{chr(9)*2}Não tem as letras: {letras_erradas}
          |||{chr(9)}{pernas}
          | |
          |||________,{chr(9)*2}Ainda há tempo! Você tem 2 tentativas! 
          | _=_==_==_|
          |/        \|
          ''')        
        
    # Adiciona a perna esquerda com 5 erros:
    elif quantidade_erros == 5:
        cabeca = "(_)"
        tronco = "/|\ "
        pernas = "/"

        # Desenha a forca: 
        print(f'''
          .___________.
          | ;_=_=_=_=_|{chr(9)*2}A resposta tem {len(resposta)} letras. 
          |||//{chr(9)} |
          |  /{chr(9)}{cabeca}
          | |{chr(9)}{tronco}{chr(9)*2}Não tem as letras: {letras_erradas}
          |||{chr(9)}{pernas}
          | |
          |||________,{chr(9)*2}Respire... você só tem 1 tentativa! 
          | _=_==_==_|
          |/        \|
          ''')
        
    # Adiciona a perna direita com 6 erros: 
    elif quantidade_erros == 6:
        cabeca = "(_)"
        tronco = "/|\ "
        pernas = "/ \ "

        # Desenha a forca: 
        print(f'''
          .___________.
          | ;_=_=_=_=_|{chr(9)*2}A resposta tinha {len(resposta)} letras. 
          |||//{chr(9)} |{chr(9)*2}
          |  /{chr(9)}{cabeca}
          | |{chr(9)}{tronco}{chr(9)*2}Não tinha as letras: {letras_erradas}
          |||{chr(9)}{pernas}
          | |
          |||________,{chr(9)*2}Oh, não! Você matou nosso amiguinho! 
          | _=_==_==_|
          |/        \|
          
          	
{chr(9)*2}         _,.-------.,_
{chr(9)*2}     ,;~'             '~;,
{chr(9)*2}   ,;                     ;,
{chr(9)*2}  ;                         ;
{chr(9)*2} ,'                         ',    ----------------
{chr(9)*2},;                           ;,  |              -----------
{chr(9)*2}; ;      .           .      ; ;  |                      -----
{chr(9)*2}| ;   ______       ______   ; |  |
{chr(9)*2}|  `/~"     ~" . "~     "~ \'  |  | 
{chr(9)*2}|  ~  ,-~~~^~, | ,~^~~~-,  ~  |  |     A RESPOSTA ERA
{chr(9)*2} |   |        |:|        |   |   |         {resposta}
{chr(9)*2} |   l       / | \       !   |   |  
{chr(9)*2} .~  (__,.--" .^. "--.,__)  ~.   |                ++++++++   
{chr(9)*2} |     ---;' / | \ `;---     |   |         ++++++++    
{chr(9)*2}  \__.       \/^\/       .__/    |  ++++++++      
{chr(9)*2}   V| \                 / |V     | /        
{chr(9)*2}    | |T~\___!___!___/~T| |      |/
{chr(9)*2}    | |`IIII_I_I_I_IIII'| |
{chr(9)*2}    |  \,III I I I III,/  |
{chr(9)*2}     \   `~~~~~~~~~~'    /
{chr(9)*2}       \   .       .   /    
{chr(9)*2}         \.    ^    ./
{chr(9)*2}           ^~~~^~~~^     
          ''')            


def ganhou():
    print('''
           ____________      
          '._==_==_=_.'     
          .-\\:      /-.    Você ganhou! Obrigada
         | (|:.     |) |    por jogar <3
          '-|:.     |-'     
            \\::.    /      
             '::. .'        
               ) (          
             _.' '._        
            '-------'
            ''')