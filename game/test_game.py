import pygame

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Button Example")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)

# Load and resize image
rosmontis = pygame.image.load('char_391_rosmon_1.png')
rosmontis = pygame.transform.scale(rosmontis, (800, 800))  # Resize to 200x200
rosmontis_rect = rosmontis.get_rect(topleft=(0, 0))  # Update position

# Font
font = pygame.font.Font(None, 36)
dialogue_font = pygame.font.Font(None, 28)

# Button dimensions
button_rect = pygame.Rect(150, 450, 600, 150)  # x, y, width, height

# Main loop
running = True
while running:
    screen.fill(BLUE)  # Clear the screen

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):  # Check if button clicked
                print("Button clicked!")

    # Add text to the button
    text_surface = font.render("charactername", True, LIGHT_BLUE)
    text_rect = text_surface.get_rect(topleft=button_rect.topleft)
    dialogue_surface = dialogue_font.render("\"hello...\"", True, WHITE)
    dialogue_rect = dialogue_surface.get_rect(topleft=(150, 500))
    screen.blit(rosmontis, rosmontis_rect)  # Blit resized image
    screen.blit(text_surface, text_rect)
    screen.blit(dialogue_surface, dialogue_rect)

    pygame.display.flip()  # Update display
    clock.tick(30)  # Limit FPS

pygame.quit()

