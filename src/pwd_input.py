import getpass

class PasswordInput:
    def password_input():
    input_text = getpass.getpass("Write your password: ")
    head = input_text[:2]
    tail = input_text[-2:]
    dot = "*"
    if len(input_text) > 5:
        print(f"\n You entered: {head}{(len(input_text)-4)*dot}{tail}\n")
    else:
        print(f"\n You entered: {len(input_text)*dot}\n")