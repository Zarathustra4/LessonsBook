from datetime import datetime

class Lesson:
    #TODO Lesson class
    def __init__(self, title, start_datetime, lesson_type, group_name, subject_title, topic_num):
        self._title = title
        self._start_datetime = start_datetime
        self._lesson_type =lesson_type
        self._group_name = group_name
        self._subject_title = subject_title
        self._topic_num = topic_num

    def get_title(self):
        return self._title
    
    def set_title(self, title):
        self._title = title


    def get_start_datetime(self):
        return self._start_datetime
    
    def set_start_datetime(self, start_datetime):
        self._start_datetime = start_datetime


    def get_lesson_type(self):
        return self._lesson_type
    
    def set_lesson_type(self, lesson_type):
        self._lesson_type = lesson_type


    def get_group_name(self):
        return self._group_name

    def set_group_name(self, group_name):
        self._group_name = group_name

    
    def get_subject_title(self):
        return self._subject_title
    
    def set_subject_title(self, subject_title):
        self._subject_title = subject_title
    

    def get_topic_num(self):
        return self._topic_num
    
    def set_topic_num(self, topic_num):
        self._topic_num = topic_num

    
    # def __repr__(self):
    #     return self._title + ", " + self._subject_title + ", " + self._group_name


    title = property(get_title, set_title)
    
    start_datetime = property(get_start_datetime, set_start_datetime)
    
    lesson_type = property(get_lesson_type, set_lesson_type)
    
    group_name = property(get_group_name, set_group_name)

    subject_title = property(get_title, set_title)

    topic_num = property(get_topic_num, set_topic_num)

if __name__ == "__main__":
    print("[Testing lesson class...]")

    l = Lesson("3d space rocket", datetime(2023, 1, 15, 12, 0), "Основна", "H2212", "Tinkercad", 5)

    print(l)