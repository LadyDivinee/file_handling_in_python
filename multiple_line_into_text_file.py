#class constructor
class MottosInLife:
    def __init__(self):
        self.file_name = "mylife.txt"
#asking the input from the user
    def enter_motto(self):
        file = open(self.file_name, "a")
#for loop asking
        while True:
            input_line = input("Hi! Enter your motto in life: ")
            print(input_line, file = file)
            options_from_user = input("Do you want to add more? Yes or No: ").lower()
            if options_from_user == "no":
                break
#finalize output
        file.close()
        print("Wow, these are inspiring! Thank you. These are saved in", self.file_name)

writer = MottosInLife()
writer.enter_motto()