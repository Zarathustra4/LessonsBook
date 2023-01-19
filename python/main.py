import connector
from group import Group
from lesson import Lesson
from enum import Enum

def main():
    run()


def decorate(funk):
    def wraper(*args, **kwargs):
        print("\n---------------------------------------------------")
        if len(args) > 0:
            print(args[0])
        print("---------------------------------------------------")
        funk(*args, **kwargs)
        print("---------------------------------------------------\n")
        
    return wraper

@decorate
def show_menu(title = "[Menu]"):
    print(
        "1) Show groups",
        "2) Show lessons...",
        "3) Show subjects",
        "4) Show price for lesson",
        "5) Calculate month salary",
        "6) Add a lesson",
        "7) Quit",
        sep = "\n"
        )

@decorate
def show_groups(title = "[Groups]"):
    groups = connector.get_groups()
    for group in groups:
        print(str(group.id) + ".", group.title + ";")

#TODO menu functions
@decorate
def show_lessons(title = "[Lessons]"):
    print("[Chose the month]")
    try:
        month = int(input(">>> "))
    except:
        print("[Wrong input, it must be an integer number!!!]")
        return
    
    if 0 < month > 12:
        print("[Wrong input, the month must be within 1 and 12!!!]")
        return
    
    lessons = connector.get_lessons_of_month(month)
    for lesson in lessons:
        print("{", lesson, "}")
     
@decorate
def calc_salary(title = "[ Salary calculation ]"):
    print("[Chose the month]")
    try:
        month = int(input(">>> "))
    except:
        print("[Wrong input, it must be an integer number!!!]")
        return
    
    if 0 < month > 12:
        print("[Wrong input, the month must be within 1 and 12!!!]")
        return
    
    print(len(connector.get_lessons_of_month(month)) * Lesson.PRICE, "грн")

def chose_subject(print_subs = True):
    subjects = connector.get_subjects()
    count = 1
    for sub in subjects:
        print(str(count) + ".", sub)
        count += 1

    print("Chose one of existed subjects or add new")
    subject = input(">> ")
    
    if subject.isalnum():
        sub_int = int(subject)
        if 0 < sub_int <= count:
            print("Chosen subject -", subjects[sub_int - 1])
            return subjects[sub_int - 1]
        else:
            raise Exception("Wrong input, subject number is out of range")
    else:
        print("Add new subject to database? [y/n]")
        ans = input(">> ")
        if ans.lower() == "y":
            connector.add_subject(subject)
            return subject
        else:
            return " "    
    

def chose_group(print_groups = True):
    groups = connector.get_groups()
    count = 1
    for group in groups:
        print(str(count) + ".", group)
        count += 1

    print("Chose one of existed subjects or add new")
    group = input(">> ")

    if group.isalnum():
        group_int = int(group)
        if 0 < group_int <= count:
            print("Chosen subject -", groups[group_int - 1])
            return groups[group_int - 1]
        else:
            raise Exception("Wrong input, group number is out of range")
    else:
        print("Add new group to database? [y/n]")
        ans = input(">> ")
        if ans.lower() == "y":
            connector.add_group(group)
            return group
        else:
            return " "


def str_to_date(date_str):
    date_str = date_str.split("-")
    if date_str != 3:
        raise Exception("Wrong date input")
    
    date

@decorate
def add_lesson(title = "[ Add a lesson ]"):
    topic = input("Print topic\n>> ")
    date_str = input("Print date\n>> ")
    count = 0
    subject = None
    while not subject:
        if count == 3:
            answer = input("Continue? [y/n]\n>> ")
            if answer.lower() == "y":
                count = 0
            elif answer.lower() == "n":
                return " "
        subject = chose_subject(not bool(count))
        count += 1

    count = 0
    group = None
    while not group:
        if count == 3:
            answer = input("Continue? [y/n]\n>> ")
            if answer.lower() == "y":
                count = 0
            elif answer.lower() == "n":
                return " "
        group = chose_group(not bool(count))
        count += 1

    try:
        topic_num = int(input("Print topic num>> "))
    except:
        print("Must be integer number!!!")
    
    print("Does the lesson need to be worked out? [y/n]")
    need_work_out = False
    ans = input(">> ")
    if ans.lower() == "y":
        need_work_out = True
    elif ans.lower() == "n":
        need_work_out = False
    else:
        print("Wrong input!!!")

    #TODO end this function and create function in connector
        

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
        elif mode == "7" or mode.upper() == "Q":
            print("[ End of work ]")
            exit()
        else:
            print("Wrong input!!!")

    


if __name__ == "__main__":
    main()