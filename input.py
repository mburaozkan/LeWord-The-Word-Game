from colorama import Fore
import english_words
import time


# Does the jobs with the inputs
class Input:

    @staticmethod
    def quit_ani():
        print()
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

    #  Checks the inputs for the secret codes to take action.
    @staticmethod
    def check_input(ipt, plc="menu"):
        # checks if user wants to quit game
        if ipt.lower() == "/quit":
            Input.quit_ani()
            exit(0)
        # checks if user wants to return menu
        elif ipt.lower() == "/menu":
            print()
            return "m"
        # checks if user want to use joker in game
        elif ipt == "/joker" and plc == "game":
            return "j"
        else:
            return ""

    # ask user to select mode for game
    @staticmethod
    def ask_mode():
        mode = input(Fore.GREEN + "::" + Fore.RESET + "For single word mode enter" +
                     Fore.BLUE + " 'one'" + Fore.RESET + " or " + Fore.BLUE + "'1'" + Fore.RESET + "/// multi"
                     " word mode enter " + Fore.MAGENTA + " 'multi'\n" + Fore.BLUE + "--> " + Fore.RESET)
        # looks for valid input
        if mode.lower() not in ['one', '1', 'multi', '/quit', '/menu']:
            mode = input(Fore.RED + "Please enter a valid choice\n--> " + Fore.RESET)
        imp = Input.check_input(mode)
        # returns menu according to input
        if imp == "m":
            return False, False, False

        word_count = 1
        # looks user wants to play which mode
        if mode.lower() == "multi":
            word_count = input(Fore.GREEN + "::" + Fore.RESET + "Enter the word count you want to play\n" +
                               Fore.BLUE + "-->" + Fore.RESET).lower()
            # looks for valid input
            if int(word_count.lower()) not in range(3, 10):
                word_count = input(Fore.RED + "Please enter a choice between 3 to 10: \n--> " + Fore.RESET)
            imp = Input.check_input(word_count)
            if imp == "m":
                return False, False, False

        lc = input(Fore.GREEN + "::" + Fore.RESET + "Enter the letter count you want to play\n" +
                    Fore.BLUE + "-->" + Fore.RESET).lower()
        print()

        # looks for valid input
        if lc not in ['/menu', '/quit']:
            if lc == "" or int(lc.lower()) not in range(3, 10):
                lc = input(Fore.RED + "Please enter a choice between 3 to 10: \n--> " + Fore.RESET)
        imp = Input.check_input(lc)
        if imp == "m":
            return False, False, False

        # returns the mode and its info to play
        return int(lc), mode, int(word_count)

    # Gets user guess for the word(s)
    @staticmethod
    def ask_user_input(length, i):
        # asks input until a valid result returned
        while True:
            guru = input(Fore.GREEN + "::" + Fore.RESET + "Enter a {}-letter Word :".format(length))
            if i % 2 == 0:
                print(Fore.MAGENTA)
            else:
                print(Fore.BLUE)

            # checks if valid
            imp = Input.check_input(guru, plc="game")
            if imp == "m":
                return False
            elif imp == "j":
                return "JOKER"

            # checks if the word is meaningful or not
            check_word = (lambda word: word.lower() in [i.lower() for i in english_words.english_words_alpha_set])

            # checks if the word length is valid or not
            if type(guru) != str or len(guru) != length:
                print(Fore.RED + 'Invalid Entry' + Fore.RESET)
                continue
            elif not check_word(guru):
                print(Fore.RED + "Please enter a meaningful word" + Fore.RESET)
            else:
                return guru.upper()
