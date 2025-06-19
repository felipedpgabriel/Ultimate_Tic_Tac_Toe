"""
Script: tic_tac_toe.py
Author: Felipe de Paula Gabriel
Date: 2024-06-09
Version : 1.0
Description: Modulo para a classe TIcTacToe.
"""

from typing import Literal
from .game_elements.board import Board

class TicTacToe:
    """
    Classe para gerenciar o funcionamento de um jogo da velha tradicional.
    """

    def __init__(self, first_player: Literal["X", "O"]="X"):
        """
        Construtor da classe TicTacToe.

        Args:
            first_player (str, optional): Elemento do primeiro jogador "X" ou "O". Defaults to "X".
        """
        self.__board = Board()
        # TODO: lançar exceção para caso "first_player" não seja nem X nem O.
        self.__current_player = first_player
        self.__game_over = False
        self.__result = ""
        self.__last_position = None

    def __swap_player(self):

        if self.__current_player == "X":
            self.__current_player = "O"
        else:
            self.__current_player = "X"

    def __choose_square(self) -> int:

        print(f"Jogador {self.__current_player}, escolha uma das casas abaixo:")

        while True:
            self.__board.print_board()

            try:
                square = int(input(">>> "))
                square_value = self.__board.get_sqaure(square)

            except KeyError as error:
                print(
                    f"Casa {error.args[0]} inexistente!\nFavor escolher uma das casas disponíveis:")

            except ValueError:
                print(
                    "Argumento inválido!\nFavor escolher uma das casas numéricas disponíveis")

            else:
                if not square_value:
                    self.__board.set_square(square, self.__current_player)
                    self.__last_position = square
                    return square

                print(
                    f"A casa {square} já foi escolhida!\nFavor escolher uma das casas disponíveis:")

    def game_ends(self) -> bool:
        """
        Método get para o atributo __terminou.

        Returns:
            bool: Indicar se o jogo terminou.
        """
        return self.__game_over

    def get_result(self) -> str:

        return self.__result

    def get_last_position(self) -> int:

        return self.__last_position

    def analyze_game(self, square: int):
        """
        Verifica o resultado a cada jogada.

        Args:
            square (int): Posição do tabuleiro escolhida.
        """

        row, column = self.__board.index_square(square)

        # TODO: identificar velha antes de preencher as casas. Modifica o atributo __result
        # TODO: Cuidar para não finalizar o jogo -> no Ultimate faz sentido jogar com velha -> menos no caso de velha geral

        if self.__board.won_in_a_line(row, self.__current_player) or self.__board.won_in_a_column(column, self.__current_player):

            self.__result = self.__current_player
            self.__game_over = True

        elif row == column:  # diagonal principal

            if self.__board.won_at_main_diagonal(self.__current_player):
                self.__result = self.__current_player
                self.__game_over = True

        elif row + column == 2:
            if self.__board.won_at_antidiagonal(self.__current_player):
                self.__result = self.__current_player
                self.__game_over = True

        elif self.__board.is_board_full():

            self.__result = "Velha"
            self.__game_over = True

    def play(self):
        """
        Método para iniciar o jogo.
        """

        while not self.__game_over:

            square = self.__choose_square()
            self.analyze_game(square)
            if not self.__game_over:
                # TODO: alterar swap_player para receber jogador da vez
                self.__swap_player()

        self.__board.print_board()

        if self.__result == "Velha":
            print("Ninguém ganhou, DEU VELHA!!!")
        else:
            print(f"Parabéns {self.__result}! VOCE VENCEU!!!")
