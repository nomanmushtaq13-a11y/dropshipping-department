import sys

from src.commands.products import run as products
from src.commands.suppliers import run as suppliers
from src.commands.search import run as search
from src.commands.stats import run as stats

COMMANDS = {
    "products": products,
    "suppliers": suppliers,
    "search": search,
    "stats": stats
}

def help_menu():
    print("""
Dropshipping Department CLI

Available Commands

products
suppliers
search
stats
""")

def main():

    if len(sys.argv) < 2:
        help_menu()
        return

    cmd = sys.argv[1]

    if cmd not in COMMANDS:
        print("Unknown Command")
        help_menu()
        return

    COMMANDS[cmd]()

if __name__ == "__main__":
    main()
