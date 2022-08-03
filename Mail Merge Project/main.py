# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Got all names in a list format
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

# Replacing the "[name]" with actual names given
with open("./Input/Letters/starting_letter.txt") as start_letter_file:
    start_letter = start_letter_file.read()
    for name in names:

        # Remove the \n in name
        stripped_name = name.strip("\n")
        letter_with_name = start_letter.replace("[name]", stripped_name)

        # Creating a file of each person's letter
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
            file.write(letter_with_name)