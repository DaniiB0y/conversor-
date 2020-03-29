import string
from random import randint
import platform
import os


texto = input('Texto para ser convertido: ')

def limpar():
    if platform.system() == "Linux":
        os.system('clear')
    else:
        os.system('cls')
def im():
    global texto
    texto = texto.title()
    print(f"{texto}")

def swap():
    global texto
    swaptexto = texto.swapcase()
    print(f"{swaptexto}")
    
def up():
    print(texto.upper())
    
def lower():
    print(texto.lower())
    
def randomizar():
# Abaixo o comando randomizar, não tá funcionando mas acho que esse é o caminho
#
#    global texto
#    y = len(texto) - 1
#    c = 0
#    while c < y:
#        random = randint(0, y)
#        texto += texto[random].upper()
#        c += 1
#
    print("Em breve")
while True:
    choice = int(input("""
    RANDOMIZAR: 1
    DIMINUIR: 2
    AUMENTAR: 3
    TROCAR: 4
    CADA PALAVRA EM MAIUSCULA: 5
    NOVO TEXTO = 6
    """))
    if choice == 1:
        limpar()
        randomizar()
    elif choice == 2:
        limpar()
        lower()
    elif choice == 3:
        limpar()
        up()
    elif choice == 4:
        limpar()
        swap()
    elif choice == 5:
        limpar()
        im()
    elif choice == 6:
        limpar()
        texto = input("Novo texto ~>")

