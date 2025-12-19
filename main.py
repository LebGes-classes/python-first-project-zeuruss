from maze import Maze
from player import Player
from game_renderer import GameRenderer


class MainGame:
    """Класс для управления основной логикой игры."""
    
    def __init__(self) -> None:
        """Инициализация игры."""
        pass
    
    def run(self) -> None:
        """Запуск основного игрового цикла."""
        level = 1
        
        while level <= 3:
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
        
        print("\nПоздравляем! Все уровни пройдены!")



print("=== ИГРА ЛАБИРИНТ ===\n"
        "Цель: дойти до выхода (X)\n"
        "Управление: WASD - движение\n"
        "Нажмите Enter чтобы начать!")

input()
    
game = MainGame()
game.run()