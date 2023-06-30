from csv_reader import ReadCsv
from test.test_dao import TestDao


class TestCarDao(TestDao):

    def setUp(self):
        self.prepare()
        self.deleteAll()
        self.create_manufacturers()

    def test_create_cars(self):
        self.reader = ReadCsv("./config/cars.csv", ",")
        row = self.reader.read()
        while row is not None:
            self.carDao.create(row)
            # manufacturer,brand,name,type,price
            in_db = self.carDao.get_by_brand_and_name_and_type(row)
            self.assertIsNotNone(in_db, "Car not found.")
            row = self.reader.read()
