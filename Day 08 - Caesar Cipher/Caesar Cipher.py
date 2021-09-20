import art

print(art.logo)

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = list(map(str.upper,lower_letters))
alphabet=2*lower_letters+2*upper_letters

again=""

def caesar(alphabet=alphabet,new_msg=""):

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction!='encode' and direction!='decode':
        direction = input("Please type a valid option ('encode' or 'decode'):\n")

    text = input("Type your message:\n")

    shift = input("Type the shift number:\n")
    while isinstance(shift,int)==False:
        if shift.isnumeric()==False:
            shift = input("The shift has to be an integer. Please type a valid shift:\n")
        elif float(shift)==int(shift):
            shift=int(shift)
        else:
            shift = (input("The shift has to be an integer. Please type a valid shift:\n"))

    while shift>26:
        shift-=26

    for i in range(len(text)):

        if text[i] in alphabet:
            if direction=="encode":
                new_msg+=alphabet[alphabet.index(text[i])+shift]
            elif direction=="decode":
                new_msg+=alphabet[26+alphabet.index(text[i])-shift]
        else:
            new_msg+=text[i]
            
    if direction=="encode":
        print(f"Here is the encoded result: {new_msg}")
    elif direction=="decode":
        print(f"Here is the decoded result: {new_msg}")

caesar()
again=input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()

while again!="no":
    if again=="yes":
        caesar()
        again=input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
    else:
        while again !='yes' and again != "no":
            again=input("Please type a valid option ('yes' or 'no') ").lower()