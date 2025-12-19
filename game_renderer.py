import os


class GameRenderer:
    """Класс для отрисовки игры в консоли."""

    @staticmethod
    def draw(maze, player, level, moves) -> None:
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
        
        print(f"\nУровень: {level}/3")
        print(f"Шагов: {moves}")
        print("Управление: WASD - движение, R - рестарт, Q - выход")