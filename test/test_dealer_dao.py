from test.test_dao import TestDao
from csv_reader import ReadCsv


class TestDealerDao(TestDao):

    def setUp(self):
        self.prepare()
        self.deleteAll()

    def test_create_dealers(self):
        self.reader = ReadCsv("./config/dealers.csv", ",")
        row = self.reader.read()
        while row is not None:
            self.dealerDao.create(row)
            in_db = self.dealerDao.get_by_name(row["dealer"])
            self.assertIsNotNone(in_db, "Dealer not found.")
            row = self.reader.read()
