import importlib
import os
import re

gbl = globals()


def showMainMenu():
    run = 1

    while run:
        print("1- Voir les solutions")
        print("2 - Voir les crédits")
        print("q - Sortir du programme")
        choose = input("Saissisez votre réponse").strip()
        if choose == "1":
            runADay()
        elif choose == "2":
            showCredit()
        elif choose == "q":
            run = 0
        else:
            print("non")


def showCredit():
    print('credit')


def runADay():
    list_folder = []
    for ele in os.listdir('.'):
        if os.path.isdir(ele):
            if re.match('^(D)[0-2][0-9]$', ele):
                list_folder.append(ele)

    unvalid_choose = 1

    while unvalid_choose:
        [print(f'{i + 1}) {x}') for i, x in enumerate(list_folder)]
        choosed_day = input("Veuillez selectionner un jour (1,2...) : ").strip()
        if choosed_day.isdigit() and list_folder[int(choosed_day) - 1]:
            day = list_folder[int(choosed_day) - 1]
            openDay(day)
            unvalid_choose = 0
        else:
            print(f'Le nombre {choosed_day} n\'existe pas')


def openDay(path_folder):
    gbl[path_folder] = importlib.import_module(f'{path_folder}.{path_folder}')
    day = getattr(globals()[path_folder], 'D01')()
    print(day.part1())
    print(day.part2())


if __name__ == '__main__':
    showMainMenu()
