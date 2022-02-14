import importlib
import os
import re

gbl = globals()


def showMainMenu():
    run = 1

    while run:
        print("1 - See solutions of every day")
        print("2 - See credits")
        print("q - Exit the program")
        choose = input("Enter a choose : ").strip()
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

    list_folder.sort()
    unvalid_choose = 1

    while unvalid_choose:
        [print(f'{i + 1}) {x}') for i, x in enumerate(list_folder)]
        choosed_day = input("Select a day (1,2...) : ").strip()
        if choosed_day.isdigit() and list_folder[int(choosed_day) - 1]:
            day = list_folder[int(choosed_day) - 1]
            openDay(day)
            unvalid_choose = 0
        else:
            print(f'The day {choosed_day} doesn\'t exist')


def openDay(path_folder):
    gbl[path_folder] = importlib.import_module(f'{path_folder}.{path_folder}')
    day = getattr(globals()[path_folder], path_folder)()
    print(f"Part 1 answer : {day.part1()}")
    print(f"Part 2 answer : {day.part2()}")
    input("Press any key to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    showMainMenu()
