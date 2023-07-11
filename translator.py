# This program contains two txt files:
#  test.txt is a sample text file that I used as the input file.
#  output.txt will contain the converted text after the program finishes running.


"""
This function converts a word to a Pig Latin
parameters: 
input(str) a word that we want to convert
Returns: 
str: The converted form of the input 
"""


def convert_to_pig_latin(input):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    suffix = []
    prefix = []
    newWord = []
    for i, c in enumerate(input):
        if c in vowels:
            suffix.append("ay")
            prefix = prefix + list(input[i:])
            newWord = prefix + suffix
            return ''.join(newWord)

        if not c in vowels:
            suffix.append(c)


print(convert_to_pig_latin("cow"))
print(convert_to_pig_latin("desk"))


"""
This function converts a text to Pig Latin 
parameters: 
text(str) a text that we want to convert
Returns: 
str: The converted form of the text  
"""


def text_to_word(text):
    words = text.split()

    pig_latin_allWords = [convert_to_pig_latin(input) for input in words]
    pig_latin_allWords = ' '.join(pig_latin_allWords)

    return pig_latin_allWords


print(text_to_word("cow eats grass"))

try:
    with open("test.txt", "r") as file:
        text = file.read()
        pig_latin_text = text_to_word(text)

        with open("output.txt", "w") as output_file:
            output_file.write(pig_latin_text)

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print(f"An error occurred: {e}")
