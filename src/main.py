import sys

from src.commands.products import run as products

COMMANDS = {
    "products": products,
}

def help_menu():
    print("""
Dropshipping Department CLI

Commands

products    View Product Database

Example

python src/main.py products
""")

def main():

    if len(sys.argv) < 2:
        help_menu()
        return

    command = sys.argv[1]

    if command not in COMMANDS:
        print("Unknown command")
        help_menu()
        return

    COMMANDS[command]()

if __name__ == "__main__":
    main()
