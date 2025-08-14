import sys
import pygame
from pygame import Surface, Rect, font as pygame_font

# Constants
CELL_WIDTH: int = 64
CELL_HEIGHT: int = 64

# Number of columns in the game
NUM_COLS: int = 10

# Number of rows in the game
NUM_ROWS: int = 10

GRID_WIDTH: int = CELL_WIDTH * NUM_COLS
GRID_HEIGHT: int = CELL_HEIGHT * NUM_ROWS

# Constants related to the text area
TEXTAREA_HEIGHT: float = 240.0
TEXTAREA_WIDTH: float = float(GRID_WIDTH)
TEXTAREA_HORIZONTAL_MARGIN: float = 20.0
FONT_SIZE: float = 24.0

# Number of lines of text that can be displayed
NUM_TEXT_LINES: int = int(TEXTAREA_HEIGHT / FONT_SIZE)

class GameApplication:
    """Main game application class."""
    
    def __init__(self) -> None:
        from game import Game
        Game()

        pygame.init()
        self.screen: Surface = pygame.display.set_mode(
            (GRID_WIDTH, int(GRID_HEIGHT + TEXTAREA_HEIGHT))
        )
        pygame.display.set_caption("Fundies Homework 9")
        
        # Load font
        try:
            self.font: pygame_font.Font = pygame_font.Font("data/fonts/default.otf", int(FONT_SIZE))
        except FileNotFoundError:
            # Fallback to default font if custom font not found
            self.font = pygame_font.Font(None, int(FONT_SIZE))
        
        # Initialize audio system (equivalent to minim)
        pygame.mixer.init()
        
        # Set up Mob audio system
        from mob import Mob
        Mob.minim = pygame.mixer  # Or your preferred audio system
        
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.running: bool = True
    
    def handle_events(self) -> None:
        """Handle pygame events."""
        from game import Game
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                else:
                    # Map pygame keys to string names
                    key_name = self._get_key_name(event.key)
                    Game.GAME.player.last_key_pressed = key_name
                    Game.GAME.tick()
    
    def _get_key_name(self, key: int) -> str:
        """Convert pygame key constants to string names."""
        key_mapping = {
            pygame.K_RIGHT: "arrow-right",
            pygame.K_LEFT: "arrow-left", 
            pygame.K_UP: "arrow-up",
            pygame.K_DOWN: "arrow-down",
            pygame.K_s: "s",
            pygame.K_a: "a",
            pygame.K_w: "w",
            pygame.K_z: "z",
            pygame.K_SLASH: "/",
            pygame.K_SPACE: "space"
        }
        return key_mapping.get(key, pygame.key.name(key))
    
    def render_grid(self) -> None:
        """Render the game grid."""
        from game import Game
        
        for x in range(NUM_COLS):
            for y in range(NUM_ROWS):
                image = Game.GAME.get_image(x, y)
                if image is not None:
                    # If using pygame surfaces for images:
                    if isinstance(image, Surface):
                        self.screen.blit(
                            image,
                            (x * CELL_WIDTH, y * CELL_HEIGHT)
                        )
                    # If image is a file path (placeholder from Entity class):
                    elif isinstance(image, str):
                        try:
                            loaded_image = pygame.image.load(image)
                            self.screen.blit(
                                loaded_image,
                                (x * CELL_WIDTH, y * CELL_HEIGHT)
                            )
                        except pygame.error:
                            # Draw a placeholder rectangle if image fails to load
                            pygame.draw.rect(
                                self.screen,
                                (128, 128, 128),  # Gray color
                                (x * CELL_WIDTH, y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
                            )
    
    def render_text(self) -> None:
        """Render the text area at the bottom of the screen."""
        from game import Game
        
        # Clear text area
        text_area_rect = Rect(
            0,
            GRID_HEIGHT,
            GRID_WIDTH,
            int(TEXTAREA_HEIGHT)
        )
        pygame.draw.rect(self.screen, (0, 0, 0), text_area_rect)  # Black background
        
        # Render text lines
        text_lines = Game.GAME.text_to_print[-NUM_TEXT_LINES:]  # Get last N lines
        y_offset = GRID_HEIGHT + int(FONT_SIZE)
        
        for line in text_lines:
            if line.strip():  # Only render non-empty lines
                text_surface = self.font.render(line, True, (255, 255, 255))  # White text
                self.screen.blit(
                    text_surface,
                    (int(TEXTAREA_HORIZONTAL_MARGIN), y_offset)
                )
            y_offset += int(FONT_SIZE)
    
    def run(self) -> None:
        """Main game loop."""
        while self.running:
            self.handle_events()
            
            # Clear screen
            self.screen.fill((0, 0, 0))  # Black background
            
            # Render game elements
            self.render_grid()
            self.render_text()
            
            # Update display
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()
        sys.exit(0)

def main() -> None:
    """Starts a game."""
    app = GameApplication()
    app.run()

if __name__ == "__main__":
    main()