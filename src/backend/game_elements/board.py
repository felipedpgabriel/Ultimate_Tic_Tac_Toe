"""
Módulo para a Classe Board.
"""

class Board:
    """
    Classe para tabuleiro do jogo.
    """

    __SQUARE_MAP = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2]
    }
    """
    Relação entre o número das casas do tabuleiro e sua posição [linha, coluna].
    """

    def __init__(self):
        """
        Construtor da classe Board.
        """
        # TODO : definir condicoes iniciais do tabuleiro
        self.__squares = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def set_square(self, square: int, value: str):

        r, c = self.index_square(square)

        self.__squares[r][c] = value

    def index_square(self, num_square: int) -> tuple[int, int]:
        """
        Retorna a posição da casa, de acordo o seu número correspondente.

        Args:
            num_square (int): Número escolhido da casa.

        Returns:
            tuple[int, int]: Posição da casa no tabuleiro [linha, coluna].
        """

        return self.__SQUARE_MAP[num_square][0], self.__SQUARE_MAP[num_square][1]

    def is_board_full(self) -> bool:
        """
        Verifica se o tabuleiro está vazio.

        Returns:
            bool: Booleano para a resposta.
        """

        for row in self.__squares:

            if any(not square for square in row):

                return False

        return True

    def print_board(self):
        """
        Escreve o tabuleiro no terminal.
        """

        print("Mapa casas\tTabuleiro")

        for r in range(0, 3):

            print(end=f" |{(r+1)*3 - 2}|{(r+1)*3 - 1}|{(r+1)*3}|\t ")
            print(end="|")

            for c in range(0, 3):

                square_value = self.__squares[r][c]

                if square_value:
                    print(end=f"{square_value}|")
                else:
                    print(end=" |")

            print("\n")

    def get_sqaure(self, num_square: int):

        row, column = self.index_square(num_square)

        return self.__squares[row][column]

    def won_in_a_line(self, row: int, value: str) -> bool:
        """
        Verifica se o jogador venceu em uma linha.

        Args:
            row (int): Posição da linha.
            value (str): Simbolo do jogador da vez.

        Returns:
            bool: Booleano para a resposta.
        """

        return all(self.__squares[row][i] == value for i in range(0, 3))

    def won_in_a_column(self, column: int, value: str) -> bool:
        """
        Verifica se o jogador venceu em uma coluna.

        Args:
            column (int): Posição da linha.
            value (str): Simbolo do jogador da vez.

        Returns:
            bool: Booleano para a resposta.
        """

        return all(self.__squares[i][column] == value for i in range(0, 3))

    def won_at_main_diagonal(self, value: str) -> bool:
        """
        Verifica se o jogador venceu na diagonal principal.

        Args:
            value (str): Simbolo do jogador da vez.

        Returns:
            bool: Booleano de resposta.
        """

        return all(self.__squares[i][i] == value for i in range(0, 3))

    def won_at_antidiagonal(self, value: str) -> bool:
        """
        Verifica se o jogador ganhoou na diagonal secundária.

        Args:
            value (str): Simbolo do jogador da vez.

        Returns:
            bool: Booleano de resposta.
        """

        return all(self.__squares[i][2-i] == value for i in range(0, 3))
