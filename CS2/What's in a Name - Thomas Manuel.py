#  ***
# Program:     What's In a Name
# Author:      Thomas Manuel
# Date:        9/30/26
# Description: An interactive command-line program that performs various string 
#              manipulations on user-inputted names
#  ***



import random

def reverse(name):
    result = ""
    for i in range(len(name) - 1, -1, -1):
        result = result + name[i]
    return result


def vowel_counter(name):
    count = 0
    for i in range(len(name)):
        if name[i] in "AIUEOaieuo":
            count = count + 1
    return count


def consonant_counter(name):
    count = 0
    for i in range(len(name)):
        if name[i] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxy":
            count = count + 1
    return count


def return_first_name(name):
    parts = name.strip().split()
    if len(parts) > 0:
        return parts[0]
    return "No name provided"


def return_middle_name(name):
    parts = name.strip().split()
    if len(parts) > 2:
        return " ".join(parts[1:-1])
    return "No middle name"


def return_last_name(name):
    parts = name.strip().split()
    if len(parts) >= 2:
        return parts[-1]
    return "No last name"


def hyphen_searcher(name):
    parts = name.strip().split()
    if parts:
        return "-" in parts[-1]
    return False


def to_lowercase(name):
    result = ""
    for i in range(len(name)):
        code = ord(name[i])
        if code >= 65 and code <= 90:
            result = result + chr(code + 32)
        else:
            result = result + name[i]
    return result


def to_uppercase(name):
    result = ""
    for i in range(len(name)):
        code = ord(name[i])
        if code >= 97 and code <= 122:
            result = result + chr(code - 32)
        else:
            result = result + name[i]
    return result


def randomize_name(chars):
    shuffled = random.sample(chars, len(chars))
    for i in range(len(chars)):
        chars[i] = shuffled[i]
    
    result = ""
    for char in chars:
        result += char
    return result


    


def main():
    while True:
        name = input("This is the main menu, what is your name? ")
        print("1 reverse ")
        print("2 vowel ")
        print("3 consonant ")
        print("4 first name ")
        print("5 middle name ")
        print("6 last name ")
        print("7 Hyphensearcher")
        print("8 to lowercase")
        print("9 to uppercase")
        print("10 create random name")
        print("11 exit")
        choice = input("Choose a number ")

        if choice == "1":
            print(reverse(name))
        elif choice == "2":
            print(vowel_counter(name))
        elif choice == "3":
            print(consonant_counter(name))
        elif choice == "4":
            print(return_first_name(name))
        elif choice == "5":
            print(return_middle_name(name))
        elif choice == "6":
            print(return_last_name(name))
        elif choice == "7":
            print(hyphen_searcher(name))
        elif choice == "8":
            print(to_lowercase(name))
        elif choice == "9":
            print(to_uppercase(name))
        elif choice == "10":
            print(randomize_name(name))
        elif choice == "11":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
