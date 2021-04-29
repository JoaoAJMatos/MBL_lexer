import os

def presentation():
    print("Matos Basic Lexer (v - 0.1) | João Matos\n")

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
