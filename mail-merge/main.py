#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt") as names:
    recipients = names.readlines()


with open("Input/Letters/starting_letter.txt") as template:
    letter_contents = template.read()
    # print(letter_contents)
    for recipient in recipients:
        rec = recipient.strip()
        new_letter = letter_contents.replace("[name]", rec)
        with open(f"Output/ReadyToSend/letter_for_{rec}.txt", "w") as to_send:
            to_send.write(new_letter)