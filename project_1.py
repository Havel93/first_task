import time

"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jakub Havel
email: havel8jakub@seznam.cz
discord: Kuba H.#6482
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
print("$ python projekt1.py")
user_name = input("username: ")
password = input("password: ")
name = {"bob":"123", "ann":"pass123", "mike":"pasword123", "liz":"pass123",}
if name.get(user_name) == password:
    print("-" * 35)
    print("Welcome to the app,", user_name, "\n" "We have 3 texts to be analyzed.")
    time.sleep(2)
    print("-" * 35)
    value = (input("Enter a number btw. 1 and 3 to select:"))
    if value in ["1", "2", "3"]:
        the_text = TEXTS[int(value) - 1]
        the_text = the_text.replace("\n", " ").replace(".", " ").replace(",", " ").replace("-", " ").split(" ")
        the_text = [marks for marks in the_text if marks != '']
        for slova in the_text:
            words = ""
            words += slova

        numbers = []
        cap = []
        small = []
        first_cap = []
        for word in the_text:
            if word.isnumeric():
                numbers.append(word)
            elif word.isupper():
                cap.append(word)
            elif word.islower():
                small.append(word)
            else:
                first_cap.append(word)
        print("There are", len(the_text), "words in the selected text." "\n" "There are", len(first_cap), "titlecase words.")
        print("There are", len(cap), "uppercase words." "\n" "There are", len(small), "lowercase words.")
        print("There are", len(numbers), "numeric strings.")
        addition = 0
        for number in numbers:
            addition += int(number)
        print("The sum of all the numbers", addition)

        length_w_dictionary = {}
        for length in the_text:
            length_w = len(length)
            if length_w in length_w_dictionary:
                length_w_dictionary[length_w] += 1
            else:
                length_w_dictionary[length_w] = 1
        print("-" * 35)
        time.sleep(2)
        print("LEN|  OCCURENCES      |NR.")
        print("-" * 35)
        for long, vyskyt in sorted(length_w_dictionary.items()):
            stars = vyskyt * "*"
            graf = "{:3}|{:18}|{:2}".format(long, stars, vyskyt)
            time.sleep(1)
            print(graf)

    else:
        print("Incorrect value, terminating the program..")
else:
    print("unregistered user, terminating the program..")
