# to install and activate the .venv folder, type "python -m venv .venv" in the terminal
# then ".venv\Scripts\activate" 
# lastly ".venv\Scripts\python" and "exit()" to return to the terminal
# to install packages, type "pip install pygame" in the terminal
# to run the program, type "python main.py" in the terminal
# python should be installed and the pygame packages are in the .venv/include folder\
# to start new project, make new .py file and import pygame

# the import for the module pygame from the inlcude folder
import pygame

# Set up for global variables
#////////////////////////////

# Initialize the pygame module
pygame.init()
# Set up the display with a screen size of 1280x720
screen = pygame.display.set_mode((1280, 720))
# Set the clock for the framerate
clock = pygame.time.Clock()
# Set the running variable for the game while loop
running = True

#////////////////////////////
# End of set up


# Main game loop
#////////////////////////////
# Running keeps the game loop going and is the boolean true
while running:
    # Exiting the game using the event structure with the QUIT event of the close window button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")


    # draw a circle that can move with the arrow keys here
    #////////////////////////////



    #////////////////////////////


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

#////////////////////////////
# End of main game loop

# Quit the program when the running loop has ended
pygame.quit()