import pandas

#TODO 1. Create a dictionary in this format:

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alpha = {row.letter:row.code for (index, row) in data.iterrows()}
print(nato_alpha)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
spelling = [nato_alpha[letter] for letter in word if letter in nato_alpha]
print(spelling)
