from english_words import english_words_alpha_set
from colorama import Fore
import random


# Does the jobs with the words
class Word:

    # Picks random words for the game
    @staticmethod
    def pick_random_word(letter_count, word_count=1):

        # uses english_word library to create a list of words
        r = [i for i in english_words_alpha_set]

        # looks for single or multi word mode
        if word_count == 1:
            true_word = ""

            # uses random library to choose randomly from 'r'
            while len(true_word) != letter_count:
                true_word = random.choice(r)
        else:
            # if mode is multi creates a list of true words
            true_word = []

            while len(true_word) < word_count:
                chosen_word = ""
                # uses random library to choose randomly from 'r'
                while len(chosen_word) != letter_count:
                    chosen_word = random.choice(r)
                true_word.append(chosen_word)

        # print(true_word)
        # returns the true word(s)
        return true_word

    # builds the table to show the user how well they guess
    @staticmethod
    def build_df(attempt, guess_arr, i, mode=1):

        # creates variables to align items in table
        result = " " * 7
        if i % 2 == 0:
            idx = Fore.MAGENTA + 'TRY ' + str(attempt + 1) + ":" + " " * 2 + Fore.RESET
        else:
            idx = Fore.BLUE + 'TRY ' + str(attempt + 1) + ":" + " " * 2 + Fore.RESET

        # makes the changes according to the mode
        if mode == 1:

            # if mode single then it just does the table at the length of the word
            cols = ['L' + str(i + 1) + " " for i in range(len(guess_arr))]
            for _ in cols:
                result += _
            result += "\n{}".format(idx)

            # prints user guess
            for _ in guess_arr:
                result += _
        else:

            # if mode multi then it does the tale at length word time word count
            cols = ['L' + str(i + 1) + " " for i in range(int(len(guess_arr)/mode))]
            for i in range(mode):
                for _ in cols:
                    result += _
                result += " "*5
            result += "\n{}".format(idx)

            # prints user guess
            for _ in guess_arr:
                result += _
        # Lastly adds the attempts left
        if mode == 1:
            if i % 2 == 0:
                result += Fore.MAGENTA + ":::{} Attempts left:::".format(len(guess_arr) - attempt) + Fore.RESET
            else:
                result += Fore.BLUE + ":::{} Attempts left:::".format(len(guess_arr) - attempt) + Fore.RESET
        else:
            if i % 2 == 0:
                result += Fore.MAGENTA + ":::{} Attempts left:::".format(len(guess_arr)//mode - attempt + 4) + Fore.RESET
            else:
                result += Fore.BLUE + ":::{} Attempts left:::".format(len(guess_arr)//mode - attempt + 4) + Fore.RESET

        # returns the 'result'
        return result

    # marks the letters according to their situation
    # with coloring them using 'coloroma' library
    @staticmethod
    def mark_letters(guess_idx, mode=1):

        final = []

        # Firstly looks for the mode
        if mode == 1:
            # then marks the letters if found or in somewhere else and appends them to 'final'
            for item in guess_idx:
                if item[2] == 'YES':
                    final.append(Fore.GREEN + item[0] + Fore.RESET + " " * 2)
                elif item[2] == 'EX':
                    final.append(Fore.YELLOW + item[0] + Fore.RESET + " " * 2)
                else:
                    final.append(item[0].lower() + " " * 2)
        else:
            # then marks the letters if found or in somewhere else and appends them to 'final'
            for index, element in enumerate(guess_idx):
                for item in element:
                    if item[2] == 'YES':
                        final.append(Fore.GREEN + item[0] + Fore.RESET + " " * 2)
                    elif item[2] == 'EX':
                        final.append(Fore.YELLOW + item[0] + Fore.RESET + " " * 2)
                    else:
                        final.append(item[0].lower() + " " * 2)
                if index != len(guess_idx) - 1:
                    final.append(" ||  ")

        # returns the 'final'
        return final
