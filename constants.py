from typing import Final

# Game constants
SCREEN_WIDTH: Final[int] = 800
SCREEN_HEIGHT: Final[int] = 600
FPS: Final[int] = 60

# Colors in RGB
WHITE: Final[tuple[int, int, int]] = (255, 255, 255)
BLACK: Final[tuple[int, int, int]] = (0, 0, 0)
RED: Final[tuple[int, int, int]] = (255, 0, 0)
GREEN: Final[tuple[int, int, int]] = (0, 255, 0)
BLUE: Final[tuple[int, int, int]] = (0, 0, 255)

# Game states
enum GameState: int:
    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2

# Movement speed constants
PLAYER_SPEED: Final[float] = 5.0
ENEMY_SPEED: Final[float] = 3.0

# Difficulty multipliers
EASY_DIFFICULTY: Final[float] = 0.5
NORMAL_DIFFICULTY: Final[float] = 1.0
HARD_DIFFICULTY: Final[float] = 1.5