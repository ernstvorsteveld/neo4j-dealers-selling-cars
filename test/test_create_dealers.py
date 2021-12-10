import unittest
import create_dealers as cd
import csv_reader as cr
from driver import Driver


class TestCreateDealers(unittest.TestCase):

    def setUp(self):
        self.driver = Driver("bolt://localhost:7687", "neo4j", "Pass*w0rd!")

    def test_create_dealers(self):
        creator = cd.CreateDealers(self.driver)
        self.reader = cr.ReadCsv("./test/read_test.csv", ",")
        row = self.reader.read()
        while row is not None:
            print(row)
            creator.create(row)
            row = self.reader.read()

    def __del__(self):
        self.reader.close()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
