from neo4j import GraphDatabase


class Driver:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def get(self):
        return self.driver

    def close(self):
        self.driver.close()

    def __del__(self):
        self.close()
