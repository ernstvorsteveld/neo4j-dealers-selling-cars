import csv_reader_functional as rf
import dao.manufacturer_dao as manufacturer_dao
import dao.dealer_dao as dealer_dao
import dao.car_dao as car_dao


class SetupNeo4j(object):

    def __init__(self, driver, files):
        self.driver = driver
        self.files = files

    def run(self):
        for key, value in self.files:
            reader = rf.ReadCsvFunctional(value, ",", None)
            reader.read_and_handle_one(self.get(key))

    def get(self, key):
        if key == "manufacturer":
            return manufacturer_dao.ManufacturerDao(self.driver).create
        if key == "dealer":
            return dealer_dao.DealerDao(self.driver).create
        if key == "car":
            return car_dao.CarDao(self.driver).create
