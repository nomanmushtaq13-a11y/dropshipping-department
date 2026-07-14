import sys

from src.commands.products import run as products
from src.commands.suppliers import run as suppliers
from src.commands.search import run as search
from src.commands.stats import run as stats
from src.commands.ranking import run as ranking
from src.commands.export import run as export
from src.commands.pipeline import run as pipeline
from src.commands.research import run as research
from src.commands.queue import run as queue

COMMANDS = {
    "products": products,
    "suppliers": suppliers,
    "search": search,
    "stats": stats,
    "ranking": ranking,
    "export": export,
    "pipeline": pipeline,
    "research": research,
    "queue": queue
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
pipeline
research
queue
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help_menu()
        sys.exit(0)

    COMMANDS.get(sys.argv[1], help_menu)()
