import sys

from src.commands.products import run as products
from src.commands.suppliers import run as suppliers

COMMANDS={

"products":products,

"suppliers":suppliers

}

if len(sys.argv)<2:

    print("Commands:")
    print(" products")
    print(" suppliers")
    exit()

cmd=sys.argv[1]

COMMANDS.get(cmd,lambda:print("Unknown Command"))()
