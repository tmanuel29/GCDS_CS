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
    parts = name.split(" ")
    return parts[0]

def return_middle_name(name):
    parts = name.split(" ")
    return parts[1]

def return_last_name(name):
    parts = name.split(" ")
    return parts[2]




def main():
    while True:
        name = input("This is the main menu, what is your name? ")
        print("1 reverse ")
        print("2 vowel ")
        print("3 consonant ")
        print("4 first name ")
        print("5 middle name ")
        print("6 last name ")
        print("7 exit")
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
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
