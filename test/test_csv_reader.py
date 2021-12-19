import unittest
import csv_reader as cr


class TestReadCsv(unittest.TestCase):

    def test_read(self):
        reader = cr.ReadCsv("./test/test-csv-reader.csv", ",", None)
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
        reader = cr.ReadCsv("./test/test-csv-reader.csv", ",")
        row = reader.read()
        while row is not None:
            row = reader.read()
        reader.close()


if __name__ == '__main__':
    unittest.main()