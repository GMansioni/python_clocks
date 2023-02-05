import pygame
import time
import math

# Initialize Pygame
pygame.init()

# Set screen size to full screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Set clock properties
clock_radius = 300
clock_position = (screen.get_width() // 2, screen.get_height() // 2)

while True:
    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour % 12
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw clock face
    pygame.draw.circle(screen, (0, 0, 0), clock_position, clock_radius, 1)

    # Draw hour hand
    hour_angle = math.radians(360 / 12 * (hour + minute / 60))
    hour_x = clock_position[0] + math.sin(hour_angle) * clock_radius * 0.5
    hour_y = clock_position[1] - math.cos(hour_angle) * clock_radius * 0.5
    pygame.draw.line(screen, (0, 0, 0), clock_position, (hour_x, hour_y), 8)

    # Draw minute hand
    minute_angle = math.radians(360 / 60 * (minute + second / 60))
    minute_x = clock_position[0] + math.sin(minute_angle) * clock_radius * 0.8
    minute_y = clock_position[1] - math.cos(minute_angle) * clock_radius * 0.8
    pygame.draw.line(screen, (0, 0, 0), clock_position, (minute_x, minute_y), 5)

    # Draw second hand
    second_angle = math.radians(360 / 60 * second)
    second_x = clock_position[0] + math.sin(second_angle) * clock_radius * 0.9
    second_y = clock_position[1] - math.cos(second_angle) * clock_radius * 0.9
    pygame.draw.line(screen, (255, 0, 0), clock_position, (second_x, second_y), 2)

    # Update the screen
    pygame.display.update()

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
