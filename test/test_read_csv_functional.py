import unittest
import csv_reader_functional as rf


class TestReadCsvFunctional(unittest.TestCase):

    def setUp(self):
        self.count = 0

    def test_read(self):
        reader = rf.ReadCsvFunctional("./test/test-csv-reader.csv", ",", None)
        reader.read_and_handle(
            self.should_read_dealer_van_mossel,
            self.should_read_dealer_groningen
        )

    def should_read_dealer_van_mossel(self, row):
        self.assertEqual(row["dealer"], 'Van Mossel Automotive Groep')
        self.assertEqual(row["level"], 'TopLevel')
        self.assertEqual(row["parent"], '')

    def should_read_dealer_groningen(self, row):
        self.assertEqual(row["dealer"], 'Groningen')
        self.assertEqual(row["level"], 'SubLevel')
        self.assertEqual(row["parent"], 'Van Mossel Automotive Groep')

    def test_loop(self):
        reader = rf.ReadCsvFunctional("./test/test-csv-reader.csv", ",", None)
        count = reader.read_and_handle_one(self.should_count)
        self.assertEqual(8, count)

    def should_count(self, row):
        self.count += 1
        return self.count