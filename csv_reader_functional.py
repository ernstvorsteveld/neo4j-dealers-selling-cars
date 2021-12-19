import csv
from contextlib import contextmanager


class ReadCsvFunctional:

    def __init__(self, file, delimiter=",", attrs=None):
        self.filename = file
        self.delimiter = delimiter
        self.attrs = attrs

    @contextmanager
    def open_file(self):
        f = open(self.filename, newline='')
        try:
            yield f
        finally:
            f.close()

    def read_and_handle(self, *functions):
        with self.open_file() as file:
            reader = csv.reader(file, delimiter=self.delimiter, quotechar='"')
            attributes = self.get_attributes(reader)
            for func in functions:
                func(self.read(reader, attributes))

    def read_and_handle_one(self, func):
        with self.open_file() as file:
            reader = csv.reader(file, delimiter=self.delimiter, quotechar='"')
            attributes = self.get_attributes(reader)
            row = self.read(reader, attributes)
            rows = 0
            while row is not None:
                rows = func(row)
                row = self.read(reader, attributes)
        return rows

    def get_attributes(self, reader):
        attributes = []
        if self.attrs is None:
            for x in next(reader):
                attributes.append(x)
        else:
            for x in self.attrs:
                attributes.append(x)
        return attributes

    @staticmethod
    def read(reader, attributes):
        try:
            result = {}
            row = next(reader)
            for idx, a in enumerate(attributes):
                result[a] = row[idx]
            return result
        except:
            return None
