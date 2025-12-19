class Player:
    """Класс для управления игроком."""

    def __init__(self, x: int, y: int) -> None:
        """
        Инициализация игрока.

        Args:
            x: Начальная X-координата игрока.
            y: Начальная Y-координата игрока.
        """

        self.__x = x
        self.__y = y
        self.__moves = 0

    def move(self, dx: int, dy: int, maze) -> bool:
        """
        Попытка переместить игрока в указанном направлении.

        Args:
            dx: Смещение по оси X.
            dy: Смещение по оси Y.
            maze: Лабиринт для проверки возможности перемещения.

        Returns:
            True, если перемещение возможно, иначе False.
        """

        new_x = self.__x + dx
        new_y = self.__y + dy
        
        if 0 <= new_x < 35 and 0 <= new_y < 21:
            if maze.get_cell(new_x, new_y) != '█':
                self.__x = new_x
                self.__y = new_y
                self.__moves += 1
                return True
        
        return False

    def get_x(self) -> int:
        """
        Получение текущей X-координаты игрока.

        Returns:
            int: X-координата игрока.
        """

        return self.__x

    def get_y(self) -> int:
        """
        Получение текущей Y-координата игрока.

        Returns:
            int: Y-координата игрока.
        """

        return self.__y

    def get_moves(self) -> int:
        """
        Получение количества совершенных ходов.

        Returns:
            int: Количество совершенных ходов.
        """

        return self.__moves