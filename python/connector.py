import mysql.connector 
from group import Group
from lesson import Lesson
from subject import Subject
from datetime import datetime

_dataBase = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="KozychDB2022"
)
cursor = _dataBase.cursor()
cursor.execute("USE lesson")


def get_groups():
    
    cursor.execute("""
        SELECT * FROM it_Group
    """)

    groups = []

    for row in cursor:
        group = Group(row[0], row[1])
        groups.append(group)

    return groups

def get_lessons_of_month(month: int):
    if not isinstance(month, int):
        raise Exception("Wrong input type, must be integer!!!")
    elif 12 < month > 0:
        raise Exception("Wrong input, must be within 1 and 12!!!")
    
    
    cursor.execute("USE lesson")
    cursor.execute(f"""SELECT topic, lesson_date, lesson_type, it_group.title, subject.title, topic_num
                    FROM lesson JOIN it_group ON lesson.group_id = it_group.id JOIN subject ON lesson.subject_id = subject.id
                    WHERE MONTH(lesson_date) = {month};""")

    lessons = []
    
    for row in cursor:
        print(row[0], row[1], row[2], row[3], row[4], row[5])
        l = Lesson(row[0], row[1], row[2], row[3], row[4], row[5])

        lessons.append(l)
    return lessons

if __name__ == "__main__":
    print("[Testing viewer...]")
    
    print(get_lessons_of_month(1))