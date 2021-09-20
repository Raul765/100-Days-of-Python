import pandas 

data = pandas.read_csv(r"Day26 - Nato Alphabet\nato_phonetic_alphabet.csv")
nato_dict={row.letter:row.code for (index,row) in data.iterrows()}

while True:
    try:
        word= input("Enter a word: ").upper()
        nato_name=[nato_dict[word[index]] for index in range(len(word))]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
    else:
        print(nato_name)
        break
