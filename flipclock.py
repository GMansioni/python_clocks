import pygame
import time

# Initialize Pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Load font for numbers
font = pygame.font.Font(None, 200)

# Define clock properties
clock_position = ((screen.get_width() // 2) - 200, (screen.get_height() // 2) - 100)
clock_spacing = 200

while True:
    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw hour tens digit
    hour_tens = hour // 10
    hour_tens_text = font.render(str(hour_tens), True, (255, 255, 255))
    screen.blit(hour_tens_text, (clock_position[0], clock_position[1]))

    # Draw hour units digit
    hour_units = hour % 10
    hour_units_text = font.render(str(hour_units), True, (255, 255, 255))
    screen.blit(hour_units_text, (clock_position[0] + clock_spacing, clock_position[1]))

    # Draw minute tens digit
    minute_tens = minute // 10
    minute_tens_text = font.render(str(minute_tens), True, (255, 255, 255))
    screen.blit(minute_tens_text, (clock_position[0] + 2 * clock_spacing, clock_position[1]))

    # Draw minute units digit
    minute_units = minute % 10
    minute_units_text = font.render(str(minute_units), True, (255, 255, 255))
    screen.blit(minute_units_text, (clock_position[0] + 3 * clock_spacing, clock_position[1]))

    # Update the screen
    pygame.display.update()

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

