class IntegerNumbers:
#class constructor
    def __init__(self):
        self.file = "integers.txt"
#instance method, read and write for the output
    def integers_in_file(self):
        file_of_integers = open(self.file, "r")
        even_file = open("double.txt", "w")
        odd_file = open("triple.txt", "w")