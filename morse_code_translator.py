#Rules for using this tool effectively
"""1 Enter what you would like to translate to (to English or to Morse Code) 2 If you are translating to English,
then separate each word with a space (' ') 3 If you are translating to Morse Code, then separate each LETTER with a
space (' ') and each WORD with a forward slash (/)"""

print("""(1) Enter what you would like to translate to (to English or to Morse Code) \n\n(2) If you are translating to English, 
then separate each word with a space (' ') \n\n(3) If you are translating to Morse Code, then separate each Morse code LETTER with a 
space (' ') and each Morse Code WORD with a forward slash (/)\n""")

morse_code_as_key = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
                     "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
                     "---": "O",
                     ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V",
                     ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}

english_as_key = {values: key for key, values in morse_code_as_key.items()}


def ask_user_questions():
    print("Your two options are: 'English' and 'Morse Code'")
    language_translating_to = ''

    while language_translating_to != 'english' or language_translating_to != 'morse code':
        language_translating_to = input("To what do you want to translate? ").lower()
        if language_translating_to == 'english':
            language_translating_from = [morse_code for morse_code in
                                         input("Type here with letters separated by a space ' ' ("
                                               ".... ._): ").split()]
            translated_word = ''
            for letters in language_translating_from:
                if letters == "/":
                    translated_word += ' '
                elif letters in morse_code_as_key.keys():
                    translated_word += morse_code_as_key[letters]
            return translated_word.capitalize()
        elif language_translating_to == 'morse code':
            language_translating_from = input("Typer here: ").upper()
            translated_word = ''
            for letter in language_translating_from:
                if letter == ' ':
                    translated_word += '  /  '
                elif letter in english_as_key.keys():
                    translated_word += english_as_key[letter]
                    translated_word += ' '
                else:
                    return "Please enter a valid character"
            return translated_word
        elif language_translating_to == 'exit':
            user_response = ""
            rerun_program(user_response)
        else:
            return "Please enter a valid option"
        

#rerun program
user_response = ""
def rerun_program(user_response):
    user_response = input("Would you like to rerun the program? ").lower()
    if user_response == "no" or user_response == "n":
        pass
    elif user_response == "yes" or user_response == "y" :
        ask_user_questions()
    else:
        print("I don't recognize your response. Please type in 'Yes' or 'No' ")


print(ask_user_questions())
print(rerun_program(user_response))

print("The program terminated successfully!")
