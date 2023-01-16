class Group:
    def __init__(self, id: int, title: str):
        self._id = id
        self._title = title
    
    def set_title(self, title):
        self._title = title
    
    def get_title(self):
        return self._title
    
    def get_id(self):
        return self._id
    
    def set_id(self, id):
        print("<<< It is impossible to change id of group!!! >>>")
        return None

    def __repr__(self) -> str:
        return "{id: " + str(self._id) + ", title: " + self._title + "}"

    title = property(get_title, set_title)
    id = property(get_id, set_id)


if __name__ == "__main__":
    h2212 = Group(1, "H2212")

    print(h2212.get_id())
    print(h2212.title)


    h2212.title = "New title"
    h2212.id = 2
    print(h2212.get_id())
    print(h2212.title)
    