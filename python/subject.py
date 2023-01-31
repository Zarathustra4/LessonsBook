class Subject:
    def __init__(self, title: str, lessons_number = 12):
        self._title = title
        self._lessons_number = lessons_number
        

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_lessons_number(self):
        return self._lessons_number

    def set_lessons_number(self, lessons_number):
        self._lessons_number = lessons_number

    def __repr__(self):
        return self._title

    title = property(get_title, set_title)
    lessons_number = property(get_lessons_number, set_lessons_number)

if __name__ == "__main__":
    s = Subject("PE")
    s.title = "Not PE"
    s.lessons_number = 10
    print(s.title, s.lessons_number)