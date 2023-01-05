from input import Input
from word import Word
from data import Data
from display import Display as dp
from colorama import Fore
import numpy as np


# The Game Object
class LeWord:

    # Only gets the mode,
    def __init__(self, mode):
        self.mode = mode

    # The joker of a word is the count of vowels and consonants in it.
    def joker(self, true_word, mode=1):
        vowels = "AEIOUaeiou"

        # checks the mode
        if mode == 1:
            vowel_c = 0
            consonant_c = 0

            # for every letter if it is vowel vowel count plus one else consonants plus one
            for letter in true_word:
                if letter in vowels:
                    vowel_c += 1
                    continue
                consonant_c += 1

            # then displays the joker for the word
            dp.display_joker(vowel_c, consonant_c, mode=mode)
        else:
            # if mode is not 1 then for every word does the same process
            for index, word in enumerate(true_word):
                vowel_c = 0
                consonant_c = 0

                # for every letter if it is vowel vowel count plus one else consonants plus one
                for letter in word:
                    if letter in vowels:
                        vowel_c += 1
                        continue
                    consonant_c += 1

                # then displays the joker for the word
                dp.display_joker(vowel_c, consonant_c, mode=mode, que=index+1)
        print()

    # starts the game with selected mode
    def play_game(self, again):

        if self.mode[2] in ["1", "one"]:
            self.single_word_game()
        else:
            self.multi_word_game()

    # the game with one-single word
    def single_word_game(self):

        # Picks the random word
        true_word = Word.pick_random_word(self.mode[1])

        # Turn true word into array of individual letters and indexes using numpy library
        true_arr = np.array(list(true_word.upper()))

        # Turn the array into [item id found] type
        true_idx = [[item, idx, None] for idx, item in enumerate(true_arr)]

        attempt = 0
        guesses = []

        # while the attempt count is less than the word length + 1
        while attempt < self.mode[1] + 1:
            # gets the guess from the user
            guess_word = Input.ask_user_input(self.mode[1], attempt)

            # looks for special inputs
            if not guess_word:
                break
            elif guess_word == "JOKER":
                self.joker(true_word, mode=self.mode[3])
                continue
            else:
                # then appends the guess
                guesses.append(guess_word)

                # Turn guess into array of individual letters and indexes using numpy library
                guess_arr = np.array(list(guess_word))

                # Turn the array into [item id found] type
                guess_idx = [[item, idx, None] for idx, item in enumerate(guess_arr)]

                matched = []
                existing = []
                # uses numpy to look if any matches between true and guess array pairs then appends to 'matching'
                matching = np.where(true_arr == guess_arr)[0]

                # for the matches between two array puts 'YES' to found
                for item in matching:
                    matched.append(guess_idx[item][0])
                    guess_idx[item][2], true_idx[item][2] = 'YES', 'YES'

                # gets the unfounded words
                rem_guess = [item for item in guess_idx if item[2] != 'YES']
                rem_true = [item for item in true_idx if item[2] != 'YES']

                # for the letters that unfounds looks if they are exist in somewhere in true word
                # if it is then marks found with 'EX'
                for guess in rem_guess:
                    for true in rem_true:
                        if guess[0] == true[0]:
                            if list(true_arr).count(guess[0]) > (matched.count(guess[0]) + existing.count(guess[0])):
                                existing.append(guess[0])
                                guess[2], true[2] = 'EX', 'EX'
                            else:
                                continue

                # Colors and marks letters based on match, exist, or not exist
                final = Word.mark_letters(guess_idx)

                # adds space to make it identical in table
                for letter in final:
                    letter += " "

                # Turn current guess into table
                guess_df = Word.build_df(attempt, final, attempt)

                print(guess_df)

                # checks whether all the letters are found or not.
                if guess_word.lower() == true_word.lower():
                    # if it is then makes the congrats
                    dp.display_cong(1, true_word=true_word.upper())
                    # and asks the user want to play again
                    again = True if input(Fore.RED + "-->" + Fore.RESET).lower() == "y" else False
                    imp = Input.check_input(str(again))
                    if imp == "m":
                        return False
                    print()
                    # finally writes the data into the csv file
                    Data.write_game_data([self.mode[2], true_word, len(true_word), attempt + 1, guesses,
                                          True if len(true_word) > attempt + 1 else False])

                    return again
                else:
                    # if not plus ones the attempt count and continues
                    attempt += 1

                    # if attempt count is at limit then
                    if attempt == self.mode[1] + 1:
                        # gives the fail message
                        dp.display_fail(1, true_word)
                        # and asks the user want to play again
                        again = True if input(Fore.RED + "-->" + Fore.RESET).lower() == "y" else False
                        imp = Input.check_input(str(again))
                        if imp == "m":
                            return False

                        print()
                        # finally writes the data into the csv file
                        Data.write_game_data([self.mode[2], true_word, len(true_word), attempt + 1, guesses,
                                              True if len(true_word) > attempt + 1 else False])
                        return again

    def multi_word_game(self):
        founded_words = []

        # Picks the random words
        true_word = Word.pick_random_word(self.mode[1], int(self.mode[3]))

        # Turn true words into array of individual letters and indexes using numpy library
        true_arr = np.array(list([j for j in i.lower()] for i in true_word))

        # Turn the array into [item id found] type
        true_idx = [[[item, idx, None] for idx, item in enumerate(element)] for element in true_arr]

        attempt = 0
        guesses_word = []

        # while the attempt count is less than the word length + 5
        while attempt < self.mode[1] + 5:
            # gets the guess from the user
            guess_word = Input.ask_user_input(self.mode[1], attempt)

            # looks for special inputs
            if not guess_word:
                break
            elif guess_word == "JOKER":
                self.joker(true_word, mode=self.mode[3])
                continue
            else:
                # then appends the guess
                guesses_word.append(guess_word)

                # Turn guess into array of individual letters and indexes using numpy library
                guess_arr = np.array(list(guess_word.lower()))

                # Turn the array into [item id found] type
                guess_idx = [[[item, idx, None] for idx, item in enumerate(guess_arr)] for i in range(int(self.mode[3]))]

                matched = []
                existing = []
                matches = []

                # for every word in true words
                for element in true_arr:
                    # uses numpy to look if any matches between true and guess array pairs then appends to 'matched'
                    matches.append(np.where(element == guess_arr)[0])

                # looks if other words founded before if it is then displays them
                for founds in founded_words:
                    index, word = founds[0], founds[1]
                    guess_idx[index] = [[item, idx, 'YES'] for idx, item in enumerate(word)]

                # for the matches between two array puts 'YES' to found
                for index, match in enumerate(matches):
                    for item in match:
                        matched.append([index, guess_idx[index][item][0]])
                        guess_idx[index][item][2], true_idx[index][item][2] = 'YES', 'YES'

                # gets the unfounded letters
                rem_guess = []
                for element in guess_idx:
                    word = []
                    for item in element:
                        if item[2] != 'YES':
                            word.append(item)
                    rem_guess.append(word)

                # gets the unfounded letters
                rem_true = []
                for element in true_idx:
                    word = []
                    for item in element:
                        if item[2] != 'YES':
                            word.append(item)
                    rem_true.append(word)

                # for the letters that unfounds looks if they are exist in somewhere in true word
                # if it is then marks found with 'EX'
                for index_g, guesses in enumerate(rem_guess):
                    for guess in guesses:
                        for index, word in enumerate(rem_true):
                            for true in word:
                                if index_g == index:
                                    if guess[0] == true[0]:
                                        if list(true_arr[index]).count(guess[0]) > \
                                                (matched.count(guess[0]) + existing.count(guess[0])):
                                            existing.append(guess[0])
                                            guess[2], true[2] = 'EX', 'EX'
                                        else:
                                            continue

                # Colors and marks letters based on match, exist, or not exist
                final = Word.mark_letters(guess_idx, mode=self.mode[3])

                # adds space to make it identical in table
                for letter in final:
                    letter += " "

                # Turn current guess into table
                guess_df = Word.build_df(attempt, final, attempt, mode=int(self.mode[3]))

                print(guess_df)

                # if any word is founded then adds them to founded words
                for index, word in enumerate(true_word):
                    if guess_word.lower() == word.lower():
                        founded_words.append([index, word])

                # checks whether all the letters are found or not.
                if len(true_word) == len(founded_words):
                    # if it is then makes the congrats
                    dp.display_cong(len(true_word), true_word=true_word)
                    # and asks the user want to play again
                    again = True if input(Fore.RED + "-->" + Fore.RESET).lower() == "y" else False
                    imp = Input.check_input(str(again))
                    if imp == "m":
                        return False

                    print()
                    # finally writes the data into the csv file
                    Data.write_game_data([self.mode[2], true_word, len(true_word), attempt + 1, guesses_word,
                                          True if len(true_word) > attempt + 1 else False])
                    return again
                else:
                    # if not plus ones the attempt count and continues
                    attempt += 1

                    # if attempt count is at limit then
                    if attempt == self.mode[1] + 5:
                        # gives the fail message
                        dp.display_fail(len(true_word), true_word)
                        # and asks the user want to play again
                        again = True if input(Fore.RED + "-->" + Fore.RESET).lower() == "y" else False
                        imp = Input.check_input(str(again))
                        if imp == "m":
                            return False

                        print()
                        # finally writes the data into the csv file
                        Data.write_game_data([self.mode[2], true_word, len(true_word), attempt + 1, guesses_word,
                                              True if len(true_word) > attempt + 1 else False])
                        return again

    # Starts the LE-WORD
    @staticmethod
    def start_le_word():

        opening = True
        again = False
        # Displays the menu for user to choose
        mode = dp.display_menu()

        # Until the user types mode 'quit' the game continues
        while mode[0] != "quit":
            # if it is not the first time and not the again after the game prints menu
            if not opening and not again:
                mode = dp.display_menu()
                if mode[0] == "quit":
                    break
            # if choice statics displays statics
            if mode[0] == "statics":
                dp.display_statics()
            # if choice rules displays rules
            elif mode[0] == "rules":
                dp.display_rules()

            opening = False

            # Creates a LeWord object
            game = LeWord(mode)

            # if the mode is play
            if mode[0] == "play":
                # then looks at the game mode
                if mode[2] in ["one", "1"]:
                    # if single then single_word_game
                    again = game.single_word_game()
                elif mode[2] == "multi":
                    # if multi then multi_word_game
                    again = game.multi_word_game()

                # after game ends if user wants to play again
                if again:
                    # asks user to play in which mode
                    a, b, c = Input.ask_mode()
                    if not mode:
                        opening = False
                        again = False
                    # assigns the mode and continues
                    mode = ["play", a, b, c]
