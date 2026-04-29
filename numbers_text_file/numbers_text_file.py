#class constructor
class NumberSeparator:
    def __init__(self, source_file_name):
        self.source_file_name = source_file_name
        self.extracted_lines = []
#open and read step
    def load_numbers_from_file(self):
        read_connection = open(self.source_file_name, "r")
        self.extracted_lines = read_connection.readlines()
        read_connection.close()
#partition and save numbers using loop and conditional statement
    def partition_and_save_numbers(self, user_select):
        if user_select == 0:
            output_filename = "even.txt"
            remainder = 0
        else:
            output_filename = "odd.txt"
            remainder = 1
        write_connection = open(output_filename, "w")

        for i in range (0, len(self.extracted_lines)):
            integer_value = int(self.extracted_lines[i].strip())
            if integer_value % 2 == remainder:
                write_connection.write(str(integer_value) + "\n")
        write_connection.close()
#main execution for user to input desired numbers
def main():
    separator = NumberSeparator("numbers.txt")
    separator.load_numbers_from_file()

    user_input = int(input("Enter 0 for even numbers, 1 for odd numbers to save: "))
    separator.partition_and_save_numbers(user_input)

    print("File created successfully!")

main()
