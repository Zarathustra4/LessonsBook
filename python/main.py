from group import Group
from lesson import Lesson
from enum import Enum
from controller import *


def main():
    run()
        

def run():
    while True:
        show_menu("[ Menu ]")
        mode = input(">>> ")
        
        if mode == "1":
            show_groups("[ Groups ]")
        elif mode == "2":
            show_lessons("[ Lessons ]")
        elif mode == "3":
            pass
        elif mode == "4":
            pass
        elif mode == "5":
            calc_salary("[ Salary calculation ]")
        elif mode == "6":
            add_lesson("[ Add a lesson ]")
        elif mode == "7":
            add_group()
        elif mode == "8" or mode.upper() == "Q":
            print("[ End of work ]")
            exit()
        else:
            print("Wrong input!!!")

    


if __name__ == "__main__":
    main()