from dao.abstract_dao import AbstractDao


class CarDao(AbstractDao):

    def create(self, car):
        # manufacturer,brand,name,type,price
        with self.driver.get().session() as session:
            session.write_transaction(self._create, car)
            session.write_transaction(self._create_manufacturer_relation, car)

    def get_by_brand_and_name_and_type(self, criteria):
        with self.driver.get().session() as session:
            data = session.read_transaction(self._get_by_brand_and_name_and_type, criteria)
            return self.handle_single_result(data)

    @staticmethod
    def _get_by_brand_and_name_and_type(tx, criteria):
        return tx.run(
            "MATCH (n:Car) WHERE n.name=$name AND n.type=$type " +
            "RETURN id(n) as id,n LIMIT 1 "
            , name=criteria["name"], type=criteria["type"]
        ).single()

    @staticmethod
    def _create(tx, car):
        tx.run("CREATE (n:Car {name: $name, type: $type}) ", name=car["name"], type=car["type"])

    @staticmethod
    def _create_manufacturer_relation(tx, car):
        tx.run(
            "MATCH (c:Car),(m:Manufacturer) "
            "WHERE c.name = $name AND m.name = $manufacturer "
            "CREATE (m) - [pc:BUILDS {}] -> (c)"
            , name=car["name"], manufacturer=car["manufacturer"]
        )
