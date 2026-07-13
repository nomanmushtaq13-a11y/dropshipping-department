try:
    from src.commands.products import run as products
except ImportError:
    products = None

try:
    from src.commands.suppliers import run as suppliers
except ImportError:
    suppliers = None

from src.commands.search import run as search

COMMANDS = {
    "products": products,
    "suppliers": suppliers,
    "search": search
}

if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd in COMMANDS and COMMANDS[cmd]:
        COMMANDS[cmd]()
    else:
        print(f"Command '{cmd}' not found or not configured.")
