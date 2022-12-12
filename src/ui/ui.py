from os import system, name
from time import sleep
import sys

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
                print("generate")

            if input_text in keywords_validate:
                UI.clear()
                print("validate")

            if input_text in keywords_browse:
                UI.clear()
                print("list of passwords")

        print("Sorry, but that isn't a valid input. Please enter a valid input or type help to see all the valid commands.")

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
if __name__ == "__main__":
    UI.fancy_input()