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