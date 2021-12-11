import unittest
from dao.dealer_dao import DealerDao
from csv_reader import ReadCsv
from driver import Driver


class TestDealerDao(unittest.TestCase):

    def setUp(self):
        self.driver = Driver("bolt://localhost:7687", "neo4j", "Pass*w0rd!")

    def test_create_dealers(self):
        dao = DealerDao(self.driver)
        self.reader = ReadCsv("./test/read_test.csv", ",")
        row = self.reader.read()
        while row is not None:
            dao.create(row)
            in_db = dao.get_by_name(row["dealer"])
            self.assertIsNotNone(in_db, "Dealer not found.")
            row = self.reader.read()

    def __del__(self):
        self.reader.close()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
