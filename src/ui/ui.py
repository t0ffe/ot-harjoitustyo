import getpass

def fancy_input():
  print("\n╔═══════════════════════════╗")
  print("║ Welcome to password-sword ║")
  print("╚═══════════════════════════╝\n")
  input_text = getpass.getpass("Enter something fancy: ")
  head = input_text[:2]
  tail = input_text[-2:]
  dot = "*"
  if len(input_text) > 5:
    print(f"\n You entered: {head}{(len(input_text)-4)*dot}{tail}\n")
  else:
    print(f"\n You entered: {len(input_text)*dot}\n")

if __name__ == "__main__":
    fancy_input()