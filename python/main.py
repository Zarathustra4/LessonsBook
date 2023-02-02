from group import Group
from lesson import Lesson
from enum import Enum
from controller import *


def main():
    run()
        

def run():
    while True:
        try:

            
            show_menu("[ Menu ]")
            mode = input(">>> ")
            
            if mode == "1":
                show_groups("[ Groups ]")
            elif mode == "2":
                show_lessons("[ Lessons ]")
            elif mode == "3":
                show_subjects("[ Subjects ]")
            elif mode == "4":
                show_price("[ PRICE ]")
            elif mode == "5":
                calc_salary("[ Salary calculation ]")
            elif mode == "6":
                add_lesson("[ Add a lesson ]")
            elif mode == "7":
                add_group("[ Add a group ]")
            elif mode == "8":
                add_subject("[ Add a subject ]")
            elif mode == "9" or mode.upper() == "Q":
                print("[ End of work ]")
                exit()
            else:
                print("Wrong input!!!")


        except Exception as ex:
            print("Your inputs caused the exception -", ex)
    


if __name__ == "__main__":
    main()