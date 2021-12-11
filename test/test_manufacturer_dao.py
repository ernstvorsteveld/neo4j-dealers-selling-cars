import unittest
from manufacturer_dao import ManufacturerDao
from csv_reader import ReadCsv
from driver import Driver


class TestCreateDealers(unittest.TestCase):

    def setUp(self):
        self.driver = Driver("bolt://localhost:7687", "neo4j", "Pass*w0rd!")

    def test_create_manufacturers(self):
        dao = ManufacturerDao(self.driver)
        self.reader = ReadCsv("./test/manufacturers.csv", ",")
        row = self.reader.read()
        while row is not None:
            print(row)
            dao.create(row)
            manufacturer = row["name"]
            in_db = dao.get_by_name(manufacturer)
            self.assertIsNotNone(in_db, "Manufacturer not found.")
            row = self.reader.read()

    def __del__(self):
        self.driver.close()
        self.reader.close()