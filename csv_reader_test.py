import unittest
import csv_reader as cr

class TestReadCsv(unittest.TestCase):

    def test_read(self):
        reader = cr.ReadCsv("read_test.csv", ",")
        row = reader.read()
        self.assertEqual(row[0], 'Van Mossel Automotive Groep')
        self.assertEqual(row[1], 'TopLevel')
        self.assertEqual(row[2], '')

        row = reader.read()
        self.assertEqual(row[0], 'Groningen')
        self.assertEqual(row[1], 'SubLevel')
        self.assertEqual(row[2], 'Van Mossel Automotive Groep')
        reader.close()

    def test_loop(self):
        reader = cr.ReadCsv("read_test.csv", ",")
        row = reader.read()
        while row != None:
            print(row)
            row = reader.read()

if __name__ == '__main__':
    unittest.main()