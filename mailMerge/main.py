# open names
# open the letter
placeholder = "[name]"
with open("./Input/Names/invited_names.txt") as names:
    # this puts the names in a list format
    name_list = names.readlines()


with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    for name in name_list:
        # remove spaces in the string
        stripped_name = name.strip()
        new_letter = content.replace(placeholder, stripped_name)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as complete_letter:
            completed = complete_letter.write(new_letter)
