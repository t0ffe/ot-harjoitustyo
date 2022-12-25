from os import system, name
from time import sleep
import sys
import string
import pwd_generator
import pwd_checker

keywords_help = {"h", "help", "man"}
keywords_input = {"i", "input", "in"}
keywords_quit = {"q", "exit", "quit", "shutdown"}
keywords_generate = {"g", "generate", "gen", "keygen"}
keywords_validate = {"v", "validate", "valid", "val", "vahvuus"}
keywords_browse = {"s", "selaa", "b", "browse"}
keywords_all = set.union(keywords_help, keywords_input, keywords_quit, keywords_generate, keywords_validate, keywords_browse)

class UI:
    def fancy_input():
        UI.clear()      
        print("\n╔══════════════════════╗")
        print("║ Welcome to pas-sword ║")
        print("╚══════════════════════╝\n")

        print("type help for manual")

        while True:
            input_text = input("What would you like to do: ")

            if input_text not in keywords_all:
                print("Sorry, but that isn't a valid input. Please enter a valid input or type help to see all the valid commands.")

            if input_text in keywords_help:
                UI.clear()
                print(f"use {keywords_help} to get this page")
                print(f"\nuse {keywords_generate} to generate password with custom parameters")
                print(f"use {keywords_validate} to see if your password is strong")
                print(f"\nuse {keywords_input} to add a password to the database")
                print(f"use {keywords_browse} to browse passwords in the database")
                print(f"\nuse {keywords_quit} to quit this program")

            if input_text in keywords_input:
                UI.clear()
                print("input")

            if input_text in keywords_quit:
                UI.clear()
                UI.print_slowly("bye bye")
                return False
                

            if input_text in keywords_generate:
                UI.clear()
                
                pwd_length = input("How long password do you want? \n")
                while not pwd_length.isnumeric():
                    if pwd_length in keywords_quit:
                        UI.clear()
                        UI.print_slowly("bye bye")
                        return False
                    print("Sorry but that is not a number")
                    pwd_length = input("plz input number:   ")
                    
    
                charset = set()
                print("What characters would you like to use? \n")
                print("1. [A-Z]")
                print("2. [a-z]")
                print("3. [0-9]")
                
                charset_select = input()
                
                UI.character_set_selection(charset_select, charset)
                
                if not charset_select.isnumeric() or len(charset) == 0:
                    while not charset_select.isnumeric() or len(charset) == 0:
                        print("please choose a corretct character set")
                        charset_select = input()
                        UI.character_set_selection(charset_select, charset)
                

                print(pwd_generator.generate_password(pwd_length, charset))

                


            if input_text in keywords_validate:
                UI.clear()
            
                password = input("Type your password to see if it's strong! \n")
                pwd_checker.PasswordStrength.password_strength(password)


            if input_text in keywords_browse:
                UI.clear()
                print("list of passwords")

        print("Sorry, but that isn't a valid input. Please enter a valid input or type 'help' to see all the valid commands.")

    def clear():

        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


    def print_slowly(text):
        for c in text:
            print (c, end= '')
            sys.stdout.flush()
            sleep(0.2)
        print("")
        
    def character_set_selection(charset_select, charset):
        if "1" in charset_select:
            charset.update(string.ascii_uppercase)
        if "2" in charset_select:
            charset.update(string.ascii_lowercase)
        if "3" in charset_select:
            charset.update([0,1,2,3,4,5,6,7,8,9,0])

if __name__ == "__main__":
    UI.fancy_input()