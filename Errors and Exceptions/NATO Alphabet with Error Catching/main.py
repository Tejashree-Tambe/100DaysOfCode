import pandas
# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    user_word = input("Enter a word: ").upper()

    try:
        nato_code = [alphabet_dict[char] for char in user_word]

    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()

    else:
        print(nato_code)


generate_phonetic()
