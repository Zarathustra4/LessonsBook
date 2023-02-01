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

def get_subjects():
    cursor.execute("SELECT title FROM Subject")
    subjects = []
    for row in cursor:
        sub = Subject(row[0])
        subjects.append(sub)

    return subjects

def add_subject(subject_title):
    cursor.execute("USE lesson")
    cursor.execute(f"""
        INSERT INTO Subject (title, lessons_number)
        VALUES ("{subject_title}", 12);
    """)

def add_group(group_title):
    cursor.execute(f"""
        INSERT INTO IT_Group (title) VALUES ({group_title});
    """)


def find_group_id(group_name: str) -> int:
    cursor.execute(f"""
        SELECT DISTINCT id FROM IT_Group WHERE title = "{group_name}";  
    """)

    id = None
    for _ in cursor:
        id = _[0]
    return id

def find_id(table: str, title: str):
    cursor.execute(f"""
        SELECT DISTINCT id FROM {table} WHERE title = "{title}";
    """)
    
    
    id = None
    for _ in cursor:
        id = _[0]
    return id



def add_lesson(lesson: Lesson):
    row = lesson.get_tuple()

    group_name = lesson._group
    group_id = find_group_id(group_name)
    
    subject_name = lesson._subject
    subject_id = find_id("Subject", subject_name)

    year = lesson._lesson_date.year
    month = lesson._lesson_date.month if lesson._lesson_date.month > 9 else "0" + str(lesson._lesson_date.month)
    day = lesson._lesson_date.day if lesson._lesson_date.day > 9 else "0" + str(lesson._lesson_date.day)

    query = f"""
        INSERT INTO Lesson(topic, lesson_date, group_id, subject_id, topic_num, needs_working_out)
        VALUES("{row[0]}", "{year}-{month}-{day}", {group_id}, {subject_id}, {row[4]}, {row[5]});
    """
    print(query)
    cursor.execute(query)



def get_lessons_of_month(month: int):
    if not isinstance(month, int):
        raise Exception("Wrong input type, must be integer!!!")
    elif 12 < month > 0:
        raise Exception("Wrong input, must be within 1 and 12!!!")
    
    
    cursor.execute(f"""SELECT topic, lesson_date, it_group.title, subject.title, topic_num, needs_working_out 
                    FROM lesson JOIN it_group ON lesson.group_id = it_group.id JOIN subject ON lesson.subject_id = subject.id
                    WHERE MONTH(lesson_date) = {month};""")

    lessons = []
    
    for row in cursor:
        # print(type(row[2]))
        l = Lesson(row[0], row[1], row[2], row[3], row[4], row[5])

        lessons.append(l)

    return lessons


def get_lessons(year: int, month: int):
    if not isinstance(month, int) or not isinstance(year, int):
        raise Exception("Wrong input type, must be integer!!!")
    elif 12 < month > 0:
        raise Exception("Wrong input, must be within 1 and 12!!!")

    
    cursor.execute(f"""SELECT topic, lesson_date, it_group.title, subject.title, topic_num, needs_working_out 
                    FROM lesson JOIN it_group ON lesson.group_id = it_group.id JOIN subject ON lesson.subject_id = subject.id
                    WHERE MONTH(lesson_date) = {month} AND YEAR(lesson_date) = {year};""")

    lessons = []
    
    for row in cursor:
        # print(type(row[2]))
        l = Lesson(row[0], row[1], row[2], row[3], row[4], row[5])

        lessons.append(l)

    return lessons



if __name__ == "__main__":
    lesson = Lesson("Test", datetime(2023, 1, 31), "H2212", "Python Junior", 8, False)
    add_lesson(lesson)