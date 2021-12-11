import unittest
from dao.manufacturer_dao import ManufacturerDao
from csv_reader import ReadCsv
from dao.driver import Driver


class TestCreateDealers(unittest.TestCase):

    def setUp(self):
        self.driver = Driver("bolt://localhost:7687", "neo4j", "Pass*w0rd!")

    def test_create_manufacturers(self):
        dao = ManufacturerDao(self.driver)
        self.reader = ReadCsv("./test/manufacturers.csv", ",")
        row = self.reader.read()
        while row is not None:
            dao.create(row)
            in_db = dao.get_by_name(row["name"])
            self.assertIsNotNone(in_db, "Manufacturer not found.")
            row = self.reader.read()

    def __del__(self):
        self.driver.close()
        self.reader.close()