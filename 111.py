import random
import os


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

    def move(self, dx: int, dy: int, maze: Maze) -> bool:
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
        
        if 0 <= new_x < width and 0 <= new_y < height:
            if maze.get_cell(new_x, new_y) != wall:
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


class GameRenderer:
    """Класс для отрисовки игры в консоли."""

    @staticmethod
    def draw(maze: Maze, player: Player, level: int, moves: int) -> None:
        """
        Отрисовка игрового поля в консоли.

        Args:
            maze: Лабиринт для отрисовки.
            player: Объект игрока для отображения его позиции.
            level: Текущий уровень игры.
            moves: Количество совершенных ходов.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
        maze_grid = maze.get_maze()
        
        for y in range(len(maze_grid)):
            for x in range(len(maze_grid[y])):
                if x == player.get_x() and y == player.get_y():
                    print('@', end='')
                else:
                    print(maze_grid[y][x], end='')

            print()
        
        print(f"\nУровень: {level}/{levels}")
        print(f"Шагов: {moves}")
        print("Управление: WASD - движение, R - рестарт, Q - выход")


def main() -> None:
    """Основной игровой цикл."""

    level = 1
    
    while level <= levels:
        maze = Maze()

        player = Player(maze.get_start_position()[0], maze.get_start_position()[1])
        
        while True:
            GameRenderer.draw(maze, player, level, player.get_moves())
            
            if maze.get_cell(player.get_x(), player.get_y()) == 'X':
                print(f"\nУровень {level} пройден! Шагов: {player.get_moves()}")
                input("Нажмите Enter для продолжения...")
                break
            
            key = input("\nКуда идем? (WASD): ").lower()
            
            match key:
                case 'q':
                    print("Выход из игры")
                    return
                case 'r':
                    print("Рестарт уровня")
                    break
                case 'w':
                    player.move(0, -1, maze)
                case 's':
                    player.move(0, 1, maze)
                case 'a':
                    player.move(-1, 0, maze)
                case 'd':
                    player.move(1, 0, maze)
        
        level += 1
    
    print("\nПоздравляем!")


print("=== ИГРА ЛАБИРИНТ ===\n"
      "Цель: дойти до выхода (X)\n"
      "Управление: WASD - движение\n"
      "Нажмите Enter чтобы начать!")

input()

main()
