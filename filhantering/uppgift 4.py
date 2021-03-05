import random as rnd
import colorama
from colorama import Fore, Back, Style, init
init(autoreset=True)



file_name = "diceroller.txt"

def y(amount):
    dices_10 = []
    for i in range(amount):
        dices_10.append(rnd.randint(1,6))
    with open(file_name, "a") as f:
        f.write("Amount of dices: {} \n".format(amount))
        f.write("Antal Ettor: " + str(dices_10.count(1)) + " Sannolikhet: " + str(dices_10.count(1) / amount) + "\n")
        f.write("Antal Tvaor: " + str(dices_10.count(2)) + " Sannolikhet: " + str(dices_10.count(2) / amount) + "\n")
        f.write("Antal Treor: " + str(dices_10.count(3)) + " Sannolikhet: " + str(dices_10.count(3) / amount) + "\n")
        f.write("Antal Fyror: " + str(dices_10.count(4)) + " Sannolikhet: " + str(dices_10.count(4) / amount) + "\n")
        f.write("Antal Femmor: " + str(dices_10.count(5)) + " Sannolikhet: " + str(dices_10.count(5) / amount) + "\n")
        f.write("Antal Sexor: " + str(dices_10.count(6)) + " Sannolikhet: " + str(dices_10.count(6) / amount) + "\n")
        f.write("\n")

x = 1
for i in range(5):
    x *= 10
    y(x)
