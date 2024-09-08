# Variable containing the value of user's password to test against crtieria defined by functions
passwordToCheck = input("Enter your password: ")

# For loop to identify how many numbers are in a string
num_count = sum(char.isdigit() for char in passwordToCheck)

# For loop to identify non-alphanumeric characters, excluding spaces
special_char_count = sum(not char.isalnum() and not char.isspace() for char in passwordToCheck)

# For loops to count how many characters are upper or lower case 
uppercase_count = sum(char.isupper() for char in passwordToCheck)
lowercase_count = sum(char.islower() for char in passwordToCheck)


GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

#print(f"{RED}{variable}{RESET}")


def numberChecker ():
    if num_count >= 3:
        print(f"{GREEN}Your password has a good amount of numbers{RESET}")
    elif num_count >= 2:
        print(f"{YELLOW}Maybe add more numbers to your password{RESET}")
    else:
        print(f"{RED}You need more numbers in your password!{RESET}")


def specialCharCount ():
    if special_char_count >= 3:
        print(f"{GREEN}Your password has a good amount of special characters{RESET}")
    elif special_char_count >= 2:
        print(f"{YELLOW}Your password may need more special characters{RESET}")
    else:
        print(f"{RED}Your password needs special characters!{RESET}")


def upperCharChecker ():
    if uppercase_count >= 4:
        print(f"{GREEN}Your password has a lot of uppercase characters{RESET}")
    elif uppercase_count >= 3:
        print(f"{YELLOW}Has a decent amount of upercase characters{RESET}")
    else:
        print(f"{RED}You need more uppercase characters in your password!{RESET}")

def lowerCharChecker ():
    if lowercase_count >= 4:
        print(f"{GREEN}Your password has a lot of lowercase characters{RESET}")
    elif lowercase_count >= 3:
        print(f"{YELLOW}Has a decent amount of lowercase characters{RESET}")
    else:
        print(f"{RED}You need more lowercase characters in your password!{RESET}")

def lengthChecker():
    if len(passwordToCheck) >= 14:
        print(f"{GREEN}Your password's length is strong{RESET}")
    elif len(passwordToCheck) >= 12:
        print(f"{YELLOW}Your password's length is great{RESET}")
    else:
        print(f"{RED}Your password's length is weak{RESET}")


def passStrengthChecker():
    numberChecker()
    lengthChecker()
    specialCharCount()
    upperCharChecker()
    lowerCharChecker()

passStrengthChecker()