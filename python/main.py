import mysql.connector

def main():
    dataBase = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="KozychDB2022"
    )

    cursor = dataBase.cursor()

    cursor.execute("USE lesson")
    cursor.execute("""
        SELECT subject.title, it_group.title, start_time, lesson_type
        FROM Lesson JOIN Subject on lesson.subject_id = subject.id 
        join it_group on lesson.group_id = it_group.id;
    """)

    for temp in cursor:
        print(temp)

if __name__ == "__main__":
    main()