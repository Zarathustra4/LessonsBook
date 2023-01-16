import mysql.connector
import connector
from group import Group

def main():
    show_menu()


def decorate(foo):
    #TODO decorator for menu
    pass

def show_menu():
    while True:
        print(
            "1) Show groups",
            "2) Show lessons...",
            "3) Show subjects",
            "4) Show price for lesson",
            "5) Calculate month salary",
            sep = "\n"
            )
        mode = input(">>> ")
        
        if mode == "1":
            show_groups()
        elif mode == "2":
            pass
        elif mode == "3":
            pass
        elif mode == "4":
            pass
        elif mode == "5":
            pass
        else:
            print("Wrong input!!!")

    
def show_groups():
    groups = connector.get_groups()
    for group in groups:
        print(str(group.id) + ".", group.title + ";")

#TODO menu functions



if __name__ == "__main__":
    main()