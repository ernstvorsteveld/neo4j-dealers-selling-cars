from test.test_dao import TestDao
from csv_reader import ReadCsv


class TestCreateDealers(TestDao):

    def setUp(self):
        self.prepare()
        self.deleteAll()

    def test_create_manufacturers(self):
        self.reader = ReadCsv("./config/manufacturers.csv", ",")
        row = self.reader.read()
        while row is not None:
            self.manufacturerDao.create(row)
            in_db = self.manufacturerDao.get_by_name(row["name"])
            self.assertIsNotNone(in_db, "Manufacturer not found.")
            row = self.reader.read()