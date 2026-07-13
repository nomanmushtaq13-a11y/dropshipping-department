import sys

from src.commands.products import run as products
from src.commands.suppliers import run as suppliers
from src.commands.search import run as search
from src.commands.stats import run as stats
from src.commands.ranking import run as ranking
from src.commands.export import run as export

COMMANDS={
"products":products,
"suppliers":suppliers,
"search":search,
"stats":stats,
"ranking":ranking,
"export":export
}

def help_menu():

    print("""
Dropshipping Department CLI

products
suppliers
search
stats
ranking
export
""")

if len(sys.argv)<2:
    help_menu()
    exit()

COMMANDS.get(sys.argv[1],help_menu)()
