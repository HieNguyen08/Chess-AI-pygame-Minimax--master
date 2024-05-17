import pygame
import sys
from setting import Config
from screens.menu import Menu


def main():
    # initialize pygame
    pygame.init()
    pygame.font.init()
    # Set Screen not in full screen mode
    screen = pygame.display.set_mode(Config.resolution)

    # load and set icon of the main window
    loaded_icon = pygame.image.load("./assets/images/white_knight.png")
    main_icon = pygame.transform.smoothscale(loaded_icon, (Config.windowIconSize, Config.windowIconSize))
    pygame.display.set_icon(main_icon)
    MenuScreen = Menu(screen)
    MenuScreen.Run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
