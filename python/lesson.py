from datetime import datetime

class Lesson:
    #TODO Lesson class
    def __init__(self, topic, date, lesson_type, group_name, subject_title, topic_num):
        self._topic = topic
        self._date = date
        self._lesson_type =lesson_type
        self._group_name = group_name
        self._subject_title = subject_title
        self._topic_num = topic_num


    def get_topic(self):
        return self._topic
    
    def set_topic(self, topic):
        self._topic = topic


    def get_date(self):
        return self._date
    
    def set_date(self, date):
        self._date = date


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


    def __repr__(self) -> str:
        return str(self._subject_title) + " " + str(self._group_name) + " " + str(self._date) + " " + str(Lesson.PRICE) + " грн" 

    topic = property(get_topic, set_topic)
    
    date = property(get_date, set_date)
    
    lesson_type = property(get_lesson_type, set_lesson_type)
    
    group_name = property(get_group_name, set_group_name)

    subject_title = property(get_subject_title, set_subject_title)

    topic_num = property(get_topic_num, set_topic_num)

    #Price for one lesson
    PRICE = 200



if __name__ == "__main__":
    print("[Testing lesson class...]")

    l = Lesson("3d space rocket", datetime(2023, 1, 15), "Основна", "H2212", "Tinkercad", 5)

    print(l)