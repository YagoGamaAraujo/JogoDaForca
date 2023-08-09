# Projeto de um jogo da forca em python para aprendizado

# Import
from tkinter import *
import random   
from os import system, name

# Função para limpar a tela de execução
def limpa_tela():

    # Windows
    if (name == 'nt'):
        _ = system('cls')
    
    #mac ou Linux
    else:
        _ = system('clear')

# Função
def game():

    
    janela_de_jogo = Tk()
    janela_de_jogo.title("Jogo da forca")
    texto_inicial = Label(janela_de_jogo, text = "\nBem-vinde ao jogo da forca! \nAdivinhe a palavra abaixo:\nTema: Fruta\n")
    texto_inicial.grid(column = 0, row = 0, padx = 10, pady = 10)

    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'mamao', 'pera', 'maca', 'kiwi']

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Numero de chances
    chances = 6

    # Lista para as letras erradas
    letras_erradas = []

    # Loop enquanto número de chances for maior do que zero
    while chances > 0:
        
        # print
        texto = Label(janela_de_jogo, text =" ".join(letras_descobertas))
        texto.grid(column = 0, row = 1, padx = 10, pady = 10)
        
        texto = Label(janela_de_jogo, text = "\nChances restantes: " + str(chances))
        texto.grid(column = 0, row = 2, padx = 10, pady = 10)
        
        texto = Label(janela_de_jogo, text = "Letras erradas:" + ", ".join(letras_erradas))
        texto.grid(column = 0, row = 3, padx = 10, pady = 10)

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Condicional
        if "_" not in letras_descobertas:
            texto = Label(janela_de_jogo, print("\nVocê venceu! A palavra era:", palavra))
            texto.grid(column = 0, row = 4, padx = 10, pady = 10)
            break
    
    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

# Bloco main
if __name__ == "__main__":
    game()


