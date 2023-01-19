from datetime import datetime
from enum import Enum

class Lesson:
    #TODO Lesson class
    def __init__(self, topic, lesson_date, group, subject, topic_num, needs_working_out):
        self._topic = topic
        self._lesson_date = lesson_date
        self._group = group
        self._subject = subject
        self._topic_num = topic_num
        self._needs_working_out = needs_working_out

    def __repr__(self):
        s = "{ "
        if self._topic:
            s += str(self._topic)
        s += " | "
        if self._lesson_date:
            s += str(self._lesson_date)
        s += " | "
        if self._group:
            s += str(self._group)
        s += " | "
        if self._subject:
            s += str(self._subject)
        s += " | "
        if self._topic_num:
            s += str(self._topic_num)
        s += " | "
        if self._needs_working_out:
            s += "Потребує відпрацювання"
        s += " }"
        return s
    #Price for one lesson
    PRICE = 200

if __name__ == "__main__":
    print("[Testing lesson class...]")

    l = Lesson("3d space rocket", datetime(2023, 1, 15), "Основна", "H2212", "Tinkercad", 5)

    print(l)