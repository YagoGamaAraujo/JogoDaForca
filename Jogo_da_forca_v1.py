# projeto de um jogo da forca em python para aprendizado

# import
import random
from os import system, name

# Função para limpar a tela de execução
def limpa_tela():

    #windows
    if (name == 'nt'):
        _ = system('cls')
    
    #mac ou Linux
    else:
        _ = system('clear')

# Função
def game():

    limpa_tela()
    print("\nBem-vinde ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    print("Tema: Fruta\n")

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
        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas:", ", ".join(letras_erradas))

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
            print("\nVocê venceu! A palavra era:", palavra)
            break
    
    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

# Bloco main
if __name__ == "__main__":
    game()


