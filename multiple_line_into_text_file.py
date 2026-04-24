#class constructor
class MottosInLife:
    def __init__(self):
        self.filename = "mylife.txt"
#asking the input from the user
    def enter_motto(self):
        file = open(self.filename, "a")