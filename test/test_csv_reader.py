import unittest
import csv_reader as cr


class TestReadCsv(unittest.TestCase):

    def test_read(self):
        reader = cr.ReadCsv("./test/read_test.csv", ",", None)
        row = reader.read()
        self.assertEqual(row["dealer"], 'Van Mossel Automotive Groep')
        self.assertEqual(row["level"], 'TopLevel')
        self.assertEqual(row["parent"], '')

        row = reader.read()
        self.assertEqual(row["dealer"], 'Groningen')
        self.assertEqual(row["level"], 'SubLevel')
        self.assertEqual(row["parent"], 'Van Mossel Automotive Groep')
        reader.close()

    def test_loop(self):
        reader = cr.ReadCsv("./test/read_test.csv", ",")
        row = reader.read()
        while row is not None:
            print(row)
            row = reader.read()


if __name__ == '__main__':
    unittest.main()
