import pandas 

word= input("Enter a word: ").upper()

data = pandas.read_csv(r"Day26 - Nato Alphabet\nato_phonetic_alphabet.csv")
nato_dict={row.letter:row.code for (index,row) in data.iterrows()}

nato_name=[nato_dict[word[index]] for index in range(len(word))]

print(nato_name)