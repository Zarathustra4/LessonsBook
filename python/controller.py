import connector
from datetime import datetime
from lesson import Lesson

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
        "7) Add a group",
        "8) Add a subject",
        "9) Quit",
        sep = "\n"
        )

@decorate
def show_groups(title = "[Groups]"):
    groups = connector.get_groups()
    count = 1
    for group in groups:
        print(count, group, sep=". ", end=";\n")
        count += 1

#TODO menu functions
@decorate
def show_lessons(title = "[Lessons]"):
    print("[Choose the year]")
    try:
        year = int(input(">>> "))
    except:
        print("[Wrong input, it must be an integer number!!!]")
        return


    print("[Choose the month]")
    try:
        month = int(input(">>> "))
    except:
        print("[Wrong input, it must be an integer number!!!]")
        return
    
    if 0 < month > 12:
        print("[Wrong input, the month must be within 1 and 12!!!]")
        return
    


    lessons = connector.get_lessons(year, month)
    for lesson in lessons:
        print("{", lesson, "}")
     
@decorate
def show_subjects(title = "[Subjects]"):
    subjects = connector.get_subjects()
    count = 1
    for subject in subjects:
        print(count, subject, sep=". ", end=";\n")
        count += 1

@decorate
def show_price(title = "[Price]"):
    print("The price for a lesson is -", Lesson.PRICE, "грн")

@decorate
def calc_salary(title = "[ Salary calculation ]"):
    print("[Choose the year]")
    try:
        year = int(input(">>> "))
    except:
        print("[Wrong input, it must be an integer number!!!]")
        return
    

    print("[Choose the month]")
    try:
        month = int(input(">>> "))
    except:
        print("[Wrong input, it must be an integer number!!!]")
        return
    
    if 0 < month > 12:
        print("[Wrong input, the month must be within 1 and 12!!!]")
        return
    
    print(len(connector.get_lessons(year, month)) * Lesson.PRICE, "грн")



def choose_subject(print_subs = True):
    subjects = connector.get_subjects()
    count = 1
    for sub in subjects:
        print(str(count) + ".", sub)
        count += 1

    print("Choose one of existed subjects or add new")
    subject = input(">> ")
    
    try:
        sub_int = int(subject)
    except ValueError: 
        print("Add new subject to database? [y/n]")
        ans = input(">> ")
        if ans.lower() == "y":
            connector.add_subject(subject)
            return subject
        else:
            return " "
    else:
        if 0 < sub_int <= count:
            print("Chosen subject -", subjects[sub_int - 1])
            return subjects[sub_int - 1]
        else:
            raise Exception("Wrong input, subject number is out of range")

def choose_group(print_groups = True):
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

def choose(choose_table):    
    count = 0
    table = None
    while not table:
        if count == 3:
            answer = input("Continue? [y/n]\n>> ")
            if answer.lower() == "y":
                count = 0
            elif answer.lower() == "n":
                return " "
        table = choose_table(not bool(count))
        count += 1
    
    return table



def input_date():
    date_str = input("Print date [yyyy-mm-dd]\n>> ")
    date_str = date_str.split("-")
    
    if len(date_str) != 3:
        raise Exception("Wrong date input")
    
    try:
        year = int(date_str[0])
        month = int(date_str[1])
        day = int(date_str[2])
    except:
        raise Exception("[ Wrong date input!!! ]")
    
    return datetime(year, month, day)

def input_topic():
    try:
        topic_num = int(input("Print topic num\n>> "))
    except ValueError:
        print("Must be integer number!!!")
    
    return topic_num

def input_work_out():    
    print("Does the lesson need to be worked out? [y/n]")
    need_work_out = False
    ans = input(">> ")
    if ans.lower() == "y":
        need_work_out = True
    elif ans.lower() == "n":
        need_work_out = False
    else:
        print("Wrong input!!!")
    
    return need_work_out 



def commit():
    connector.commit()


@decorate
def add_lesson(title = "[ Add a lesson ]"):
    topic = input("Print topic\n>> ")

    date = input_date()

    subject = choose(choose_subject)

    group = choose(choose_group)

    topic_num = input_topic()

    need_work_out = input_work_out()

    lesson = Lesson(topic, date, group, subject, topic_num, need_work_out)

    connector.add_lesson(lesson)

@decorate
def add_group(title = "[ Add a group ]"):
    title = input("Print title of a group\n>>> ")
    connector.add_group(title)

@decorate
def add_subject(title = "[ Add a subject ]"):
    title = input("Print the title of a subject\n>> ")
    connector.add_subject(title)