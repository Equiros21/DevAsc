# JSON Birthday challenge at https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html

import json
import sys
from bs4 import beautifulsoup4

birthdays = {}

def bday(filename="JSON Birthday"):
    global birthdays
    birthdays = json.load(open(filename, "r"))
    scientist = list(dict.keys(birthdays))
    print("\nWe know the birthday of the following scientists:\n\n" + "\n".join(scientist))
    x = input("\n\nPlease select one: ")
    if x not in scientist:
        print("\nPlease select a valid choice, try again!")
        bday()
    print("Your scientist birthday is: " + dict.get(birthdays, x) + "\n")
    y = input("Would you like to add a new scientist birthday? (Y/N): ")
    while True:
        if y == "Y":
            newentry()
            break
        elif y == "N":
            print("\nGood bye!")
            sys.exit()
        else:
            print("Please select a valid choice, try again!")
            y = input('Would you like to add a new scientist birthday? (Y/N): ')


def newentry(filename="JSON Birthday"):
    global birthdays
    birthdays.update(
        {input("Please enter the scientist name and last name: "): input("Please enter the scientist birthday: ")})
    with open(filename, "w") as f:
        json.dump(birthdays, f, indent=4)


bday()
