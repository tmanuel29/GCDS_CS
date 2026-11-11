
# ***
# Program:     What's In a Name
# Author:      Thomas Manuel
# Date:        9/30/26
# Description: An interactive command-line program that performs various string
#              manipulations on user-inputted names
#Log:   1.0 - original code
#        1.1 - fixed code so that user does not have to enter name over and over
#        1.2 - added line by line documentation / not for every line / repeated lines dont have over and over - for important lines
# ***



import random                                                           # brings in Python's dice roller



def reverse(name):
    """
    Description: Reverses the characters in a string.

    Args: name (string)

    Returns: string (the reversed text)
    """
    result = ""                                                         # blank slate to build the new name
    for i in range(len(name) - 1, -1, -1):                              # walks backward from the last letter
        result = result + name[i]                                       # tacks each letter onto the end

    return result                                                       # hands back the name, flipped


def vowel_counter(name):
    """
    Description: Counts how many vowels are in a given string.

    Args: name (string)

    Returns: integer (count of vowels)
    """
    count = 0                                                           # tally starts at zero
    for i in range(len(name)):                                          # visits every character one by one
        if name[i] in "AIUEOaieuo":                                     # is it a vowel?
            count = count + 1                                           # yep, add one to the tally

    return count                                                        # final vowel score


def consonant_counter(name):
    """
    Description: Counts how many consonants are in a given string.

    Args: name (string)

    Returns: integer (count of consonants)
    """
    count = 0
    for i in range(len(name)):
        if name[i] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":     # is it a consonant?
            count = count + 1

    return count                                                        # final consonant score


def return_first_name(name):
    """
    Description: Extracts the first name from a full name.

    Args: name (string)

    Returns: string (the first name or error message)
    """
    parts = name.strip().split()                                        # trims spaces and chops the name into words
    if len(parts) > 0:                                                  # did they type anything at all?
        return parts[0]                                                 # word #1 is the first name

    return "No name provided"                                           # nothing typed, nothing to show


def return_middle_name(name):
    """
    Description: Extracts the middle name(s) from a full name.

    Args: name (string)

    Returns: string (the middle name or error message)
    """
    parts = name.strip().split()
    if len(parts) > 2:                                                  # need 3+ words to have a middle
        return " ".join(parts[1:-1])                                    # glues together everything between first and last

    return "No middle name"                                             # too short for a middle name


def return_last_name(name):
    """
    Description: Extracts the last name from a full name.

    Args: name (string)

    Returns: string (the last name or error message)
    """
    parts = name.strip().split()
    if len(parts) >= 2:                                                 # need 2+ words to have a last name
        return parts[-1]                                                # -1 grabs the very last word

    return "No last name"                                               # just one word, so no last name


def hyphen_searcher(name):
    """
    Description: Checks if the last name contains a hyphen.

    Args: name (string)

    Returns: boolean (True if hyphen found, False if not)
    """
    parts = name.strip().split()
    if parts:                                                           # only look if the list isn't empty
        return "-" in parts[-1]                                         # True if the last name has a dash

    return False                                                        # no name, no hyphen


def to_lowercase(name):
    """
    Description: Converts all uppercase letters to lowercase.

    Args: name (string)

    Returns: string (the lowercase text)
    """
    result = ""
    for i in range(len(name)):
        code = ord(name[i])                                             # turns the letter into its secret number code
        if code >= 65 and code <= 90:                                   # 65-90 is the A-Z zone
            result = result + chr(code + 32)                            # +32 shrinks it to lowercase
        else:                                                           # not a capital? leave it alone
            result = result + name[i]

    return result                                                       # the whole name, now quiet


def to_uppercase(name):
    """
    Description: Converts all lowercase letters to uppercase.

    Args: name (string)

    Returns: string (the uppercase text)
    """
    result = ""
    for i in range(len(name)):
        code = ord(name[i])
        if code >= 97 and code <= 122:                                  # 97-122 is the a-z zone
            result = result + chr(code - 32)                            # -32 pumps it up to uppercase
        else:
            result = result + name[i]

    return result                                                       # the whole name, now LOUD


def randomize_letters(chars):
    """
    Description: Randomly shuffles the characters in a name.

    Args: chars (list or string of characters)

    Returns: string (the randomized name)
    """
    # Shuffle the letters and drop them back into the list
    shuffled = random.sample(chars, len(chars))                         # scrambles a copy like a deck of cards
    for i in range(len(chars)):
        chars[i] = shuffled[i]

    # Stick the scrambled letters back together into one string
    result = ""
    for char in chars:
        result += char

    return result                                                       # the name, totally mixed up


def palindrome_searcher(name):
    """
    Description: Checks if the first name reads the same forward and backward.

    Args: name (string)

    Returns: boolean (True if first name is a palindrome, False if not)
    """
    first = return_first_name(name)                                     # only cares about the first name
    lower = to_lowercase(first)                                         # lowercase so "Anna" and "anna" match

    return lower == reverse(lower)                                      # same forwards and backwards? it's a palindrome


def get_initials(name):
    """
    Description: Gets the first letter of each word in a name.

    Args: name (string)

    Returns: string (uppercase initials separated by periods)
    """
    parts = name.strip().split()
    initials = ""                                                       # empty until we collect some letters
    for part in parts:                                                  # one word at a time
        initials = initials + part[0] + "."                             # grabs the first letter and adds a dot

    return to_uppercase(initials)                                       # capitals make initials look official


def main():
    """
    Description: Displays the menu loop and handles user choices.

    Args: None

    Returns: None
    """
    name = input("This is the main menu, what is your name? ")          # asked once, used everywhere

    while True:                                                         # the menu keeps coming back until you quit
        # Print out every option on the menu
        print("1 reverse")
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
        choice = input("Choose a number ")                              # pick your fighter

        # Match the number picked to its function, run it, and print the result
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
            print(randomize_letters(list(name)))                        # turns the name into a list so it can be shuffled
        elif choice == "11":
            print(palindrome_searcher(name))
        elif choice == "12":
            print(get_initials(name))
        elif choice == "13":
            print("Exiting the program. Goodbye!")
            break                                                       # breaks out of the loop, game over
        else:                                                           # anything that isn't 1-13 lands here
            print("Invalid choice, please try again.")


if __name__ == "__main__":                                              # only runs when you start this file directly
    main()                                                              # and we're off!
