#projeto de um jogo da forca em python para aprendizado

#import
import random
from os import system, name

#Função para limpar a tela de execução
def limpa_tela():

    #windows
    if (name == 'nt'):
        _ = system('cls')
    
    #mac ou Linux
    else:
        _ = system('clear')