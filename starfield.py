import pygame
import random

# Initialize Pygame and set up the screen.
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Starfield Simulation Screensaver")

# Number of stars in the field.
num_stars = 300

# Create a list to hold our stars.
# Each star is represented as a list: [x, y, z]
# We use a coordinate system with the origin at the center of the screen.
stars = []
for _ in range(num_stars):
    # x and y are distributed over the window (centered at 0,0)
    x = random.uniform(-width / 2, width / 2)
    y = random.uniform(-height / 2, height / 2)
    # z (depth) is a positive number; larger values mean farther away.
    z = random.uniform(1, width / 2)
    stars.append([x, y, z])

# Clock to control the frame rate.
clock = pygame.time.Clock()

# Speed at which the stars move toward the viewer.
speed = 2

running = True
while running:
    # Event loop: quit if the user closes the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with black.
    screen.fill((0, 0, 0))

    # Loop through each star in the starfield.
    for star in stars:
        # Move the star closer by decreasing its z value.
        star[2] -= speed

        # If the star has moved past the viewer, reinitialize it as if it's far away.
        if star[2] <= 0:
            star[0] = random.uniform(-width / 2, width / 2)
            star[1] = random.uniform(-height / 2, height / 2)
            star[2] = width / 2

        # Perspective projection:
        # The idea is to simulate a 3D-to-2D perspective by dividing x and y by z.
        # A scaling factor is applied so that stars "expand" as they come closer.
        factor = 200  # Adjust this factor to change the “zoom”
        x = int((star[0] / star[2]) * factor + width / 2)
        y = int((star[1] / star[2]) * factor + height / 2)

        # Only draw the star if it’s still within the window boundaries.
        if 0 <= x < width and 0 <= y < height:
            # Adjust brightness: closer stars are brighter.
            brightness = max(0, min(255, 255 - int(star[2] / (width / 2) * 255)))
            color = (brightness, brightness, brightness)

            # Optionally, vary the size of the star based on its depth.
            radius = 1 if star[2] > (width / 4) else 2
            pygame.draw.circle(screen, color, (x, y), radius)

    # Update the display.
    pygame.display.flip()
    # Limit the frame rate to 60 frames per second.
    clock.tick(60)

pygame.quit()
