import unittest
from csv_reader import ReadCsv
from dao.driver import Driver
from test.test_dao import TestDao


class TestCarDao(TestDao):

    def setUp(self):
        self.prepare()
        self.deleteAll()
        self.create_manufacturers()

    def test_create_cars(self):
        reader = ReadCsv("./test/cars.csv", ",")
        row = reader.read()
        while row is not None:
            self.carDao.create(row)
            # manufacturer,brand,name,type,price
            in_db = self.carDao.get_by_brand_and_name_and_type(row)
            self.assertIsNotNone(in_db, "Car not found.")
            row = reader.read()
        reader.close()

    def __del__(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
