#TODO 1. Create a dictionary in this format:

nato_data = {}
with open('nato_phonetic_alphabet.csv') as file:
    data = file.readlines()
    for i in data:
        key = i.splitlines()
        dict_type = key[0].split(',')
        nato_data.update([dict_type])

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

spelling = []
user_input = input("Enter a word: ").upper()
for item in user_input:
    if item in nato_data:
        spelling.append(nato_data[item])
print(spelling)
