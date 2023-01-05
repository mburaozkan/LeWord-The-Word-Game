from colorama import Fore
from data import Data
from input import Input
from pyfiglet import Figlet
import time


# Does the jobs that showing screens to user
class Display:

    # The opening screen for the game
    @staticmethod
    def opening():
        # uses pyfiglet library to make it look greater
        f = Figlet(font='slant')
        print(Fore.BLUE + f.renderText('     L E -'), end="")
        time.sleep(1)
        print(Fore.MAGENTA + f.renderText(' W O R D'))

        # In a for loop writes loading... screen
        time.sleep(0.5)
        print(Fore.GREEN + "                  LOADING", end="")
        for i in range(3):
            time.sleep(0.5)
            print(".", end="")
        time.sleep(0.5)
        print("\n")

    # The closing screen for the game
    @staticmethod
    def closing():
        # In a for loop uses time library for waiting process while printing
        time.sleep(0.5)
        print(Fore.RED + "                  ADIO", end="")
        for i in range(3):
            time.sleep(0.5)
            print("S", end="")
        for i in range(3):
            time.sleep(0.5)
            print(".", end="")
        time.sleep(0.5)

    # Displays the rules in general
    # uses coloroma to make it colorful
    @staticmethod
    def display_rules():
        print(Fore.BLUE + "##############################################" + Fore.RESET)
        print("                  LE-RULES                   ")
        print(Fore.MAGENTA + "##############################################" + Fore.GREEN)
        print("||--->   " + Fore.RESET + " Welcome to Le-Rules!              " + Fore.GREEN + "||")
        print("||--->   " + Fore.RESET + " To Play LeWord:                   " + Fore.GREEN + "||")
        print("||--->   " + Fore.RESET + " First enter letter count.         " + Fore.GREEN + "||")
        print("||--->   " + Fore.RESET + " Second guess the word.            " + Fore.GREEN + "||")
        print("||--->   " + Fore.RED + " Be careful!!!!    " + Fore.RESET + "                " + Fore.GREEN + "||")
        print("||--->   " + Fore.RESET + " Guess count is only               " + Fore.GREEN + "||")
        print("||--->   " + Fore.RESET + " 1/5 more than word length         " + Fore.GREEN + "||")
        print("||--->   " + Fore.RESET + " in single/multi mode.             " + Fore.GREEN + "||")
        print("||--->   " + Fore.RESET + " To use joker in game type" + Fore.BLUE + " /joker " + Fore.RESET + " " + Fore.GREEN + "||")
        print("||--->   " + Fore.RESET + " To menu anywhere type" + Fore.GREEN + " /menu " + Fore.RESET + "      " + Fore.GREEN + "||")
        print("||--->   " + Fore.RESET + " To quit anywhere type" + Fore.RED + " /quit " + Fore.RESET + "      " + Fore.GREEN + "||\n" + Fore.RESET)
        # uses time library to make a time space for user
        input(Fore.MAGENTA + "||--> Press 'Enter' to return menu          ||\n" + Fore.RESET)

        time.sleep(0.5)
        print(Fore.BLUE + "-------------Returning To Menu----------------\n" + Fore.RESET)
        time.sleep(0.5)

    # Displays the statics of the user
    # uses coloroma to make it colorful
    @staticmethod
    def display_statics():
        total_attempts, total_words, total_trues, total_wrongs, \
        total_letters_writen, known_words, unknown_words, mode, most_word, most_letter = Data.read_game_data()

        print(Fore.BLUE + "##############################################" + Fore.RESET)
        print("                  LE-STATICS                  ")
        print(Fore.MAGENTA + "##############################################" + Fore.GREEN)
        print("|| " + Fore.RESET + " Total Words Played:    \u001B[34m{:5}            \u001B[32m||".format(total_words))
        print("|| " + Fore.RESET + " Total Words Found:     \u001B[35m{:5}            \u001B[32m||".format(total_trues))
        print("|| " + Fore.RESET + " Total Words Unfound:   \u001B[34m{:5}            \u001B[32m||".format(total_wrongs))
        print("|| " + Fore.RESET + " Total Attempts:        \u001B[35m{:5}            \u001B[32m||".format(total_attempts))
        print("|| " + Fore.RESET + " Total Letters Writen:  \u001B[34m{:5}            \u001B[32m||".format(total_letters_writen))
        print("|| " + Fore.RESET + " Most Used Letter:        \u001B[35m'{}' -> {:5}   \u001B[32m||".format(list(most_letter)[0], most_letter[list(most_letter)[0]]))
        print("|| " + Fore.RESET + " Most Used Word:      \u001B[34m'{:5}' ->   {:3}   \u001B[32m||\n".format(list(most_word)[0], most_word[list(most_word)[0]]))

        # uses time library to make a time space for user
        input(Fore.MAGENTA + "||--> Press 'Enter' to return menu          ||\n" + Fore.RESET)

        time.sleep(0.5)
        print(Fore.BLUE + "-------------Returning To Menu----------------\n" + Fore.RESET)
        time.sleep(0.5)

    # Displays the menu
    # uses coloroma to make it colorful
    @staticmethod
    def display_menu():
        menu_header = "a##############################################\n"\
                      "#################b"+ " LE-MENU " + "c####################\n" \
                      "##############################################b"

        menu_exp = Fore.GREEN + "||--->   " + Fore.RESET + "Welcome to Le-Word!!!!" + Fore.GREEN + "             ||\n" + \
                   "||--->   " + Fore.RESET+ "For rules insert \'rules\'" + Fore.GREEN + "           ||\n" +\
                   "||--->   " + Fore.RESET + "To play insert \'play\'." + Fore.GREEN + "             ||\n" + \
                   "||--->   " + Fore.RESET + "For statics insert \'statics\'" + Fore.GREEN + "       ||\n" + \
                   "||--->   " + Fore.RESET + "To quit insert \'quit\'" + Fore.GREEN + "              ||" + Fore.RESET

        choice_list = ["play", "quit", "statics"]

        for char in menu_header:
            time.sleep(0.01)
            if char == "a":
                print(Fore.BLUE, end="")
            elif char == "b":
                print(Fore.RESET, end="")
            elif char == "c":
                print(Fore.MAGENTA, end="")
            else:
                print(char, end="")
        print()
        print(menu_exp)

        choice = ""

        # to start the loop that will game will be played wants user to choice until the choice is 'quit'
        while choice not in choice_list:
            choice = input(Fore.LIGHTBLUE_EX + "-->" + Fore.RESET)
            print()
            # checks input
            Input.check_input(choice)

            if choice == "play":
                length, mode, word_count = Input.ask_mode()
                if not mode:
                    return ["", "", "", ""]
                return ["play", length, mode, word_count]
            elif choice == "statics":
                return ["statics", "lol"]
            elif choice == "quit":
                return ["quit", 1]
            elif choice == "rules":
                return ["rules", 0]
            else:
                print(Fore.RED + "Invalid Entry Please Choice Again!" + Fore.RESET)

    # Displays the congrats screen
    # uses coloroma to make it colorful
    @staticmethod
    def display_cong(mode, true_word=""):

        if mode == 1:
            print()
            print(Fore.BLUE + '#############################################' + Fore.RESET)
            print(f'  HURRAY THE WORD WAS: {true_word.upper()} ')
            print(Fore.MAGENTA + '#############################################' + Fore.RESET)
            print(Fore.GREEN + "||" + Fore.RESET + 'YOU ARE A HUMAN GENIUS!                  ' + Fore.GREEN + "||" + Fore.RESET)
            print(Fore.GREEN + "||" + Fore.RESET + 'YOU SHOULD BE FEARED AND RESPECTED!!     ' + Fore.GREEN + "||" + Fore.RESET)
            print(Fore.GREEN + "||" + Fore.RESET + 'Give yourself a pat on the shoulder :)   ' + Fore.GREEN + "||" + Fore.RESET)
            print(Fore.GREEN + "||" + Fore.RESET + "That student debt is finally paying off! " + Fore.GREEN + "||" + Fore.RESET)
            print(Fore.GREEN + "||" + Fore.RESET + "||WANNA PLAY AGAIN?  (" + Fore.GREEN + "y" + Fore.RESET + "/" + Fore.RED + "n" + Fore.RESET + ")               " + Fore.GREEN + "||" + Fore.RESET)
        else:
            print()
            print(Fore.BLUE + '#############################################' + Fore.RESET)
            print(f'         HURRAY YOUR RIGHTTTT:              ')
            print(Fore.MAGENTA + '#############################################' + Fore.RESET)
            print(Fore.GREEN + "||" + Fore.RESET + 'YOU ARE A HUMAN GENIUS!                  ' + Fore.GREEN + "||" + Fore.RESET)
            print(Fore.GREEN + "||" + Fore.RESET + 'YOU SHOULD BE FEARED AND RESPECTED!!     ' + Fore.GREEN + "||" + Fore.RESET)
            print(Fore.GREEN + "||" + Fore.RESET + 'Give yourself a pat on the shoulder :)   ' + Fore.GREEN + "||" + Fore.RESET)
            print(Fore.GREEN + "||" + Fore.RESET + "That student debt is finally paying off! " + Fore.GREEN + "||" + Fore.RESET)
            print(Fore.GREEN + "||" + Fore.RESET + "||WANNA PLAY AGAIN?  (" + Fore.GREEN + "y" + Fore.RESET + "/" + Fore.RED + "n" + Fore.RESET + ")               " + Fore.GREEN + "||" + Fore.RESET)

    # Displays the failure screen
    # uses coloroma to make it colorful
    @staticmethod
    def display_fail(mode, true_word):
        if mode == 1:
            print(Fore.RED + "||" + Fore.RESET + f' Sorry, gotta read more BOOKS! The word was {true_word.upper()}', end="")
        else:
            print(Fore.RED + "||" + Fore.RESET + f' Sorry, gotta read more BOOKS! The words were ', end="")
            for word in true_word:
                print(f'{word.upper()} ', end="")
        print(Fore.RED + ', OBVIOUSLY... ||' + Fore.RESET)

        print(Fore.GREEN + "||" + Fore.RESET + "WANNA PLAY AGAIN?  (" + Fore.GREEN + "y" + Fore.RESET + "/" + Fore.RED + "n" + Fore.RESET + ")               " + Fore.GREEN + "||" + Fore.RESET)

    # Displays the joker of the word to the user
    # uses coloroma to make it colorful
    @staticmethod
    def display_joker(vowels, consonant, mode=1, que=1):
        if mode == 1:
            print(Fore.MAGENTA + "<-JOKER->" + Fore.RESET + "This word has {} vowels and {} consonants!"
                  .format(vowels, consonant) + Fore.MAGENTA + "<-JOKER->" + Fore.RESET)
        else:
            print(Fore.MAGENTA + "<-JOKER->" + Fore.RESET + "{}. word has {} vowels and {} consonants!"
                  .format(que, vowels, consonant) + Fore.MAGENTA + "<-JOKER->" + Fore.RESET)
