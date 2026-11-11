# ***
# Program:     What's In a Name
# Author:      Thomas Manuel
# Date:        9/30/26
# Description: An interactive command-line program that performs various string
#              manipulations on user-inputted names
# Log:   1.0 - original code
#        1.1 - fixed code so that user does not have to enter name over and over
#        1.2 - added line by line documentation / not for every line / repeated lines dont have over and over - for important lines
# ***



import random                                                           # lets the program pick things at random



def reverse(name):
    """
    Description: Reverses the characters in a string.

    Args: name (string)

    Returns: string (the reversed text)
    """
    result = ""                                                         # starts with an empty string
    for i in range(len(name) - 1, -1, -1):                              # loops from the last character to the first
        result = result + name[i]                                       # adds each character to the result

    return result                                                       # gives back the finished string


def vowel_counter(name):
    """
    Description: Counts how many vowels are in a given string.

    Args: name (string)

    Returns: integer (count of vowels)
    """
    count = 0                                                           # starts the count at zero
    for i in range(len(name)):                                          # loops through each character
        if name[i] in "AIUEOaieuo":                                     # checks if the character is a vowel
            count = count + 1                                           # adds 1 to the count

    return count                                                        # gives back the total count


def consonant_counter(name):
    """
    Description: Counts how many consonants are in a given string.

    Args: name (string)

    Returns: integer (count of consonants)
    """
    count = 0
    for i in range(len(name)):
        if name[i] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":     # checks if it's a consonant
            count = count + 1

    return count


def return_first_name(name):
    """
    Description: Extracts the first name from a full name.

    Args: name (string)

    Returns: string (the first name or error message)
    """
    parts = name.strip().split()                                        # removes extra spaces and splits into words
    if len(parts) > 0:                                                  # makes sure at least one word was typed
        return parts[0]                                                 # the first word is the first name

    return "No name provided"                                           # runs if nothing was typed


def return_middle_name(name):
    """
    Description: Extracts the middle name(s) from a full name.

    Args: name (string)

    Returns: string (the middle name or error message)
    """
    parts = name.strip().split()
    if len(parts) > 2:                                                  # a middle name needs at least 3 words
        return " ".join(parts[1:-1])                                    # joins every word between first and last

    return "No middle name"                                             # runs if there are fewer than 3 words


def return_last_name(name):
    """
    Description: Extracts the last name from a full name.

    Args: name (string)

    Returns: string (the last name or error message)
    """
    parts = name.strip().split()
    if len(parts) >= 2:                                                 # a last name needs at least 2 words
        return parts[-1]                                                # the last word is the last name

    return "No last name"                                               # runs if there is only one word


def hyphen_searcher(name):
    """
    Description: Checks if the last name contains a hyphen.

    Args: name (string)

    Returns: boolean (True if hyphen found, False if not)
    """
    parts = name.strip().split()
    if parts:                                                           # makes sure the list isn't empty
        return "-" in parts[-1]                                         # True if the last word has a hyphen

    return False                                                        # no name means no hyphen


def to_lowercase(name):
    """
    Description: Converts all uppercase letters to lowercase.

    Args: name (string)

    Returns: string (the lowercase text)
    """
    result = ""
    for i in range(len(name)):
        code = ord(name[i])                                             # gets the character's number code
        if code >= 65 and code <= 90:                                   # 65 to 90 are the codes for A to Z
            result = result + chr(code + 32)                            # adding 32 makes it lowercase
        else:                                                           # anything that isn't a capital letter stays the same
            result = result + name[i]

    return result


def to_uppercase(name):
    """
    Description: Converts all lowercase letters to uppercase.

    Args: name (string)

    Returns: string (the uppercase text)
    """
    result = ""
    for i in range(len(name)):
        code = ord(name[i])
        if code >= 97 and code <= 122:                                  # 97 to 122 are the codes for a to z
            result = result + chr(code - 32)                            # subtracting 32 makes it uppercase
        else:
            result = result + name[i]

    return result


def randomize_letters(chars):
    """
    Description: Randomly shuffles the characters in a name.

    Args: chars (list or string of characters)

    Returns: string (the randomized name)
    """
    shuffled = random.sample(chars, len(chars))                         # makes a shuffled copy
    for i in range(len(chars)):                                         # loops through each spot in the list
        chars[i] = shuffled[i]                                          # puts the shuffled character in that spot

    result = ""
    for char in chars:                                                  # loops through each character
        result += char                                                  # adds it to the result string

    return result


def palindrome_searcher(name):
    """
    Description: Checks if the first name reads the same forward and backward.

    Args: name (string)

    Returns: boolean (True if first name is a palindrome, False if not)
    """
    first = return_first_name(name)                                     # gets just the first name
    lower = to_lowercase(first)                                         # lowercase so capitals don't matter

    return lower == reverse(lower)                                      # True if it matches its reverse


def get_initials(name):
    """
    Description: Gets the first letter of each word in a name.

    Args: name (string)

    Returns: string (uppercase initials separated by periods)
    """
    parts = name.strip().split()
    initials = ""                                                       # starts with no initials
    for part in parts:                                                  # loops through each word
        initials = initials + part[0] + "."                             # adds the first letter and a period

    return to_uppercase(initials)                                       # makes the initials capital


def main():
    """
    Description: Displays the menu loop and handles user choices.

    Args: None

    Returns: None
    """
    name = input("This is the main menu, what is your name? ")          # asks for the name once

    while True:                                                         # shows the menu until the user exits
        print("1 reverse")                                              # prints the menu options
        print("2 vowel")
        print("3 consonant")
        print("4 first name")
        print("5 middle name")
        print("6 last name")
        print("7 Hyphensearcher")
        print("8 to lowercase")
        print("9 to uppercase")
        print("10 create random list of letters")
        print("11 palindrome searcher")
        print("12 get initials")
        print("13 exit")
        choice = input("Choose a number ")                              # asks which option to run

        if choice == "1":                                               # checks which number the user picked
            print(reverse(name))                                        # runs the function and prints the answer
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
            print(randomize_letters(list(name)))                        # turns the name into a list first
        elif choice == "11":
            print(palindrome_searcher(name))
        elif choice == "12":
            print(get_initials(name))
        elif choice == "13":
            print("Exiting the program. Goodbye!")
            break                                                       # stops the loop and ends the program
        else:                                                           # any other input is not a menu option
            print("Invalid choice, please try again.")


if __name__ == "__main__":                                              # only runs when this file is run directly
    main()                                                              # starts the program
