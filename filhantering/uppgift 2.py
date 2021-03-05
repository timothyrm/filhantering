import colorama
from colorama import Fore, Back, Style

file_name = "Provresultat.txt"

with open(file_name, "r") as f:
    print("Uppgift A - DOWN BELOW:")
    for i in range(1,20):
        print(Fore.GREEN + f.readline().strip("\n"))

with open(file_name, "r+") as f:
    file_content = []
    for i in range(1,20):
        file_content.append(f.readline())
    file_content.sort()
    f.write("\n-----------------------------------------------------------")
    f.write("\n\nCODE MADE THIS CHANGES BELOW, UPPGIFT [B] OUTPUT BELOW:\n\n")
    f.write("-----------------------------------------------------------\n")
    for person in file_content:
        f.write(person)
    f.write("\n")
    print(f"UPPGIFT B WRITTEN TO {file_name}")

with open(file_name, "r+") as f:
    file_content = []
    F = []
    E = []
    D = []
    C = []
    B = []
    A = []
    for i in range(1,20):
        file_content.append(f.readline())
    for person in file_content:
        person_numbers = int(person[-3:])
        if person_numbers < 20:
            F.append(person)
        if person_numbers >= 20 and person_numbers <= 29: 
            E.append(person)
        if person_numbers >= 30 and person_numbers <= 39:
            D.append(person)
        if person_numbers >= 40 and person_numbers <= 49:
            C.append(person)
        if person_numbers >= 50 and person_numbers <= 59:
            B.append(person)
        if person_numbers >= 60 and person_numbers <= 70:
            A.append(person)
    f.write("\n-----------------------------------------------------------")
    f.write("\n\nCODE MADE THIS CHANGES BELOW, UPPGIFT [C] OUTPUT BELOW:\n\n")
    f.write("-----------------------------------------------------------\n")
    f.write("\n[A] ELEVER - GRATTIS SMÅBARN!:\n")
    for person in A:
        f.write(person)
    f.write("\n[B] ELEVER:\n")
    for person in B:
        f.write(person)
    f.write("\n[C] ELEVER:\n")
    for person in C:
        f.write(person)
    f.write("\n[D] ELEVER:\n")
    for person in D:
        f.write(person)
    f.write("\n[E] ELEVER:\n")
    for person in E:
        f.write(person)
    f.write("\n[F] DUMMA ELEVER - BETTER LUCK NEXT TIME!:\n")
    for person in F:
        f.write(person)