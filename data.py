import csv
import os


# Does the jobs with the csv files using csv library
class Data:

    # Gets the permissions needed
    @staticmethod
    def get_permissions_if_exists():
        # Calls the os to get permissions to use file 'data.csv'
        try:
            os.chmod("data.csv", 0o777)
        except FileNotFoundError:
            pass

    # opens the file named 'data.csv' if they not exist
    @staticmethod
    def open_file_if_not_exist():
        name = "data.csv"
        try:
            if open(name):
                return True
        except FileNotFoundError:
            open(name, "x")

    # writes the last game data to 'data.csv'
    @staticmethod
    def write_game_data(data):
        # first looks if it is exists
        Data.open_file_if_not_exist()
        Data.get_permissions_if_exists()

        # appends the data given to file
        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(data)

    @staticmethod
    def read_game_data():
        # first looks if it is exists
        Data.open_file_if_not_exist()
        Data.get_permissions_if_exists()

        # reads file
        with open("data.csv", "r") as file:
            reader = csv.reader(file)

            mode = 0
            total_attempts = 0
            total_words = 0
            total_trues = 0
            total_wrongs = 0
            total_letters_writen = 0
            most_word = {}
            most_letter = {}
            known_words = []
            unknown_words = []
            word_dict = {}
            letter_dict = {}

            # for every line in the file parse the datas
            for line in reader:
                if not line:
                    continue

                item = line
                mode = item[0]
                word = item[1]
                length = int(item[2])
                attempts = int(item[3])
                guesses = item[4]
                is_true = item[-1]

                total_attempts += attempts
                total_words += 1

                guesses = guesses[2:-2].split("', '")

                # and gets the general statics

                total_trues += 1 if is_true == "True" else 0
                total_wrongs += 1 if is_true == "False" else 0

                total_letters_writen += length * attempts

                if is_true == "True":
                    known_words.append(word)
                else:
                    unknown_words.append(word)

                for guess in guesses:
                    if guess not in word_dict.keys():
                        word_dict[guess] = 1
                    else:
                        word_dict[guess] += 1

                for guess in guesses:
                    for letter in guess:
                        if letter not in letter_dict.keys():
                            letter_dict[letter] = 1
                        else:
                            letter_dict[letter] += 1

            # most used word
            word_m = 0
            count_m = 0
            for word, count in word_dict.items():
                if count_m < count:
                    word_m, count_m = word, count

            most_word = {word_m: count_m}

            # most used letter
            letter_m = 0
            count_m = 0
            for letter, count in letter_dict.items():
                if count_m < count:
                    letter_m, count_m = letter, count

            most_letter = {letter_m: count_m}

            # then returns them for other functions to use
            return total_attempts, total_words, total_trues, total_wrongs, \
                total_letters_writen, known_words, unknown_words, mode, most_word, most_letter
