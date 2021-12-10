import unittest
from create_manufacturer import CreateManufacturer
from csv_reader import ReadCsv
from driver import Driver


class TestCreateDealers(unittest.TestCase):

    def setUp(self):
        self.driver = Driver("bolt://localhost:7687", "neo4j", "Pass*w0rd!")

    def test_create_manufacturers(self):
        creator = CreateManufacturer(self.driver)
        self.reader = ReadCsv("./test/manufacturers.csv", ",")
        row = self.reader.read()
        while row is not None:
            print(row)
            creator.create(row)
            row = self.reader.read()

    def __del__(self):
        self.driver.close()
        self.reader.close()


