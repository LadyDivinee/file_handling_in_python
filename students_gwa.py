#class student GWA analyzer
class StudentGwaAnalyzer:
    def __init__(self, student_file):
        self.student_file = student_file
        self.student_records = []
#load students data
    def student_data(self):
        file_connection = open(self.student_file, "r")
        self.student_records = file_connection.readlines()
        file_connection.close()
#find highest gwa
    def print_highest_gwa(self):
        top_name = ""
        lowest_number = 5.0

        for line in self.student_records:
            name, gwa = line.strip().split(",")
            gwa = float(gwa)

            if gwa < lowest_number:
                lowest_number = gwa
                top_name = name
#print output
        print("Top Student: ")
        print("Name: ", top_name)
        print("GWA:", lowest_number)
        print(f"\033[92mAng galing, sipag mo ah maangas ka!\033[0m")


def main():
    analyzer = StudentGwaAnalyzer("students.txt")
    analyzer.student_data()
    analyzer.print_highest_gwa()


main()