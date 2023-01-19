class Subject:
    def __init__(self, id, title: str, lessons_number = 12):
        self._title = title
        self._lessons_number = lessons_number
        self._id = id

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_lessons_number(self):
        return self._lessons_number

    def set_lessons_number(self, lessons_number):
        self._lessons_number = lessons_number

    def get_id(self):
        return self._id

    def set_id(self, id):
        raise Exception("It is not possible to change ID")

    def __repr__(self):
        return self._title

    title = property(get_title, set_title)
    id = property(get_id, set_id)
    lessons_number = property(get_lessons_number, set_lessons_number)

if __name__ == "__main__":
    s = Subject("PE")
    s.title = "Not PE"
    s.lessons_number = 10
    print(s.title, s.lessons_number)