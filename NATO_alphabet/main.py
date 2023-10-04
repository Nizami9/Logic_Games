import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

is_ok = False


def generate_alphabet():
        word = input("Enter a word: ").upper()
        try:
            output_list = [phonetic_dict[letter] for letter in word]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
            generate_alphabet()
        # word = input("Sorry, only letters in the alphabet please: ").upper()
        else:
            print(output_list)


generate_alphabet()