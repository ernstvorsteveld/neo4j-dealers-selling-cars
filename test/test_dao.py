import unittest
from dao.car_dao import CarDao
from dao.manufacturer_dao import ManufacturerDao
from csv_reader import ReadCsv
from dao.driver import Driver


class TestDao(unittest.TestCase):

    def prepare(self):
        self.driver = Driver("bolt://localhost:7687", "neo4j", "Pass*w0rd!")
        self.manufacturerDao = ManufacturerDao(self.driver)
        self.carDao = CarDao(self.driver)

    def create_manufacturers(self):
        self.reader = ReadCsv("./config/manufacturers.csv", ",")
        row = self.reader.read()
        while row is not None:
            self.manufacturerDao.create(row)
            row = self.reader.read()
        self.reader.close()

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
        self.driver.close()
