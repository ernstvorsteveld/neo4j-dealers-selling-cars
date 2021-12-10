import csv

class ReadCsv:

    def __init__(self, file, delimiter=",", hasHeader=True):
        self.file = open(file, newline='')
        self.csv_reader = csv.reader(self.file, delimiter=delimiter, quotechar='"')
        if hasHeader:
            print("Header: ", next(self.csv_reader))

    def close(self):
        self.file.close()

    def read(self):
        try:
            return next(self.csv_reader)
        except:
            return None

    def __del__(self):
        self.close()
