import random as rnd
simulerade_tärningar = []
for i in range(1,11):
    tärning = rnd.randint(1,6)
    simulerade_tärningar.append(tärning)
with open("diceRoll.txt", "a") as f:
    f.write("Listan osorterad: " + str(simulerade_tärningar) + "\n")
    simulerade_tärningar.sort()
    f.write("Listan sorterad: " + str(simulerade_tärningar) + "\n")
    f.write("Antal femmor: "+ str(simulerade_tärningar.count(5)) + "\n")

    