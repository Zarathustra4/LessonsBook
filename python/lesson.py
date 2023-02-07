from datetime import datetime


class Lesson:
    #TODO Lesson class
    def __init__(self, topic, lesson_date : datetime, group, subject, topic_num, needs_working_out):
        self._topic = topic
        self._lesson_date = lesson_date
        self._group = group
        self._subject = subject
        self._topic_num = topic_num
        self._needs_working_out = needs_working_out

    def get_tuple(self):
        return (self._topic, self._lesson_date, self._group, self._subject, self._topic_num, self._needs_working_out)

    def __repr__(self):
        need_work_out = "Потребує відпрацювання" if self._needs_working_out else "Не потребує відпрацювання"
        return f"{self._topic} | {self._lesson_date} | {self._group} | {self._subject} | {self._topic_num} | {need_work_out}"

    #Price for one lesson
    PRICE = 200

if __name__ == "__main__":
    import mysql.connector
    
    _dataBase = mysql.connector.connect(
            host ="localhost",
            user ="root",
            passwd ="KozychDB2022"
    )
    cursor = _dataBase.cursor()
    cursor.execute("USE gradebook;")
    
    cursor.execute("Select * from Student;")
    
    for _ in cursor:
        print(_)