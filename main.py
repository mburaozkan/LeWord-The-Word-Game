from game import LeWord
from display import Display
from data import Data
import os

#### MAIN FUNCTION ####
if __name__ == '__main__':
    # Calls the os to write to the terminal colorful.ru
    os.system("")

    # Gets the permissions to use files from cmd
    Data.get_permissions_if_exists()

    # Shows the opening screen
    Display.opening()

    # Starts the game
    LeWord.start_le_word()

    # Closes the game
    Display.closing()
