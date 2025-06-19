"""
Script: app.py
Author: Felipe de Paula Gabriel
Date: 2024-06-09
Version : 1.0
Description: Script principal do Ultimate Tic Tac Toe. A versão 1.0 é um jogo da velha tradicional
para terminal.
"""

from backend.tic_tac_toe import TicTacToe

def choose_symbol_menu() -> str:
    """
    Menu para selecionar o simbolo do primeiro jogador.

    Returns:
        str: O ou X.
    """

    print("Selecione o número do símbolo desejado:")
    print("[0] - O")
    print("[1] - X")
    symbol = int(input(">>> "))

    if symbol == 0:
        return "O"

    if symbol == 1:
        return "X"

    print("Selecione somente as opções fornecidas abaixo\n")
    return choose_symbol_menu()


if __name__ == "__main__":

    print("=========== Bem Vindo ao Jogo da Velha ===========\n")
    first_player_symbol = choose_symbol_menu()
    game = TicTacToe(first_player_symbol)
    game.play()
