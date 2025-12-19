import random


wall = '█'
path = ' '
width = 35
height = 21
levels = 3


class Maze:
    """Класс для представления и генерации лабиринта."""

    def __init__(self) -> None:
        """
        Инициализация лабиринта.
        """
        self.__maze = []
        self.__start_position = (0, 1)
        self.generate()

    def generate(self) -> None:
        """Генерация нового лабиринта."""

        self.__maze = []
        
        for row in range(height):
            new_row = []

            for col in range(width):
                new_row.append(wall)

            self.__maze.append(new_row)
        
        def carve(x: int, y: int) -> None:
            """
            Рекурсивная функция для создания проходов в лабиринте.

            Args:
                x: X-координата текущей клетки.
                y: Y-координата текущей клетки.
            """

            self.__maze[y][x] = path
            directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
            
            random.shuffle(directions)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 < nx < width - 1 and 0 < ny < height - 1 and self.__maze[ny][nx] == wall:
                    self.__maze[y + dy // 2][x + dx // 2] = path
                    carve(nx, ny)
        
        carve(1, 1)
        
        self.__maze[1][0] = path
        self.__maze[height - 2][width - 1] = 'X'
        self.__start_position = (0, 1)

    def get_maze(self) -> list:
        """
        Получение лабиринта.

        Returns:
            list: Двумерный список символов, представляющий лабиринт.
        """

        return self.__maze

    def get_start_position(self) -> tuple:
        """
        Получение стартовой позиции игрока.

        Returns:
            tuple: Кортеж (x, y) стартовой позиции.
        """

        return self.__start_position

    def get_cell(self, x: int, y: int) -> str:
        """
        Получение символа в указанной клетке.

        Args:
            x: X-координата клетки.
            y: Y-координата клетки.

        Returns:
            str: Символ в указанной клетке.
        """

        return self.__maze[y][x]