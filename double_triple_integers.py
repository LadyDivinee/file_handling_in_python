class IntegerNumbers:
#class constructor
    def __init__(self):
        self.file = "integers.txt"
#instance method, read and write for the output
    def integers_in_file(self):
        file_of_integers = open(self.file, "r")
        even_file = open("double.txt", "w")
        odd_file = open("triple.txt", "w")
#checking if even or odd
        for line in file_of_integers:
            number = int(line.strip())
            if number % 2 == 0:
                double_number = number * number
                print(double_number, file =  even_file)
            else:
                triple_number = number * number * number
                print(triple_number, file = odd_file)
#save the data
        file_of_integers.close()
        even_file.close()
        odd_file.close()
#show the final output
        print("All done! You're desired separation of numbers have been created.")

processor = IntegerNumbers()
processor.integers_in_file()