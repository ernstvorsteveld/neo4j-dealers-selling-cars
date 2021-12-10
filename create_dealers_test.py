import unittest
import create_dealers as cd
import csv_reader as cr

class TestCreateDealers(unittest.TestCase):

    def test_read(self):
        creator = cd.CreateDealers("bolt://localhost:7687", "neo4j", "Pass*w0rd!")
        reader = cr.ReadCsv("read_test.csv", ",")
        row = reader.read()
        while row != None:
            print(row)
            creator.create(row[0], row[1], row[2])
            row = reader.read()


if __name__ == '__main__':
    unittest.main()        
