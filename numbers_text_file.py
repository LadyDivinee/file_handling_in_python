class NumberSeparator:
    def __init__(self, source_filename):
        self.source_filename = source_filename
        self.extracted_lines = []

    def load_numbers_from_file(self):
        read_connection = open(self.source_filename, "r")
        self.extracted_lines = read_connection.readlines()
        read_connection.close()