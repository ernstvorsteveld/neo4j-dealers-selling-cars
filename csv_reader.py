import csv


class ReadCsv:

    def __init__(self, file, delimiter=",", attrs=None):
        self.file = open(file, newline='')
        self.csv_reader = csv.reader(self.file, delimiter=delimiter, quotechar='"')
        self.attributes = []
        if attrs is None:
            for x in next(self.csv_reader):
                self.attributes.append(x)
        else:
            for x in attrs:
                self.attributes.append(x)

    def close(self):
        self.file.close()

    def read(self):
        try:
            result = {}
            row = next(self.csv_reader)
            for idx, a in enumerate(self.attributes):
                result[a] = row[idx]
            return result
        except:
            return None

#     def __del__(self):
# # self.close()
