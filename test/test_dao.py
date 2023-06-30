import unittest
from csv_reader import ReadCsv
from dao.driver import Driver
from dao.car_dao import CarDao
from dao.manufacturer_dao import ManufacturerDao
from dao.dealer_dao import DealerDao


class TestDao(unittest.TestCase):

    def prepare(self):
        self.driver()
        self.manufacturerDao = ManufacturerDao(self.driver)
        self.carDao = CarDao(self.driver)
        self.dealerDao = DealerDao(self.driver)

    def driver(self):
        self.driver = Driver("bolt://localhost:7687", "neo4j", "Pass*w0rd!")

    def create_manufacturers(self):
        self.reader = ReadCsv("./config/manufacturers.csv", ",")
        row = self.reader.read()
        while row is not None:
            self.manufacturerDao.create(row)
            row = self.reader.read()

    def create_cars(self):
        self.reader = ReadCsv("./config/cars.csv", ",")
        row = self.reader.read()
        while row is not None:
            self.carDao.create(row)

    def deleteAll(self):
        with self.driver.get().session() as session:
            session.write_transaction(self._delete_all)

    @staticmethod
    def _delete_all(tx):
        tx.run("MATCH (n) DETACH DELETE n")

    def __del__(self):
        self.reader.close()


if __name__ == '__main__':
    unittest.main()
