from googletrans import Translator, constants
from pprint import pprint

def translator():
    # init the Google API translator
    translator = Translator()

    # translate a spanish text to english text (by default)
    translation = translator.translate(input("type here: "), src="en", dest="ar")
    output = (f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    print(output)
    restart()

def restart():
    option = input("do u wanna repeat, type y for yes and n for no: ")
    if (option == "y"):
        translator()
    else:
        print("bye")
translator()