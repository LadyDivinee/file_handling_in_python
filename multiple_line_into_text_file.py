#class constructor
class MottosInLife:
    def __init__(self):
        self.filename = "mylife.txt"
#asking the input from the user
    def enter_motto(self):
        file = open(self.filename, "a")
#for loop asking
        while True:
            input_line = input("Hi! Enter your motto in life: ")
            print(input_line, file = file)
            options_from_user = input("Do you want to add more? Yes or No: ").lower()
            if options_from_user == "no":
                break
