from abstract_dao import AbstractDao


class ManufacturerDao(AbstractDao):

    def create(self, manufacturer):
        with self.driver.get().session() as session:
            session.write_transaction(self._create_manufacturer, manufacturer)
            session.write_transaction(self._create_relation, manufacturer)

    def get_by_name(self, name):
        with self.driver.get().session() as session:
            data = session.read_transaction(self._get_by_name, name)
            return self.handle_single_result(data)

    @staticmethod
    def _get_by_name(tx, name):
        return tx.run("MATCH (n:Manufacturer) WHERE (n.name=$name) return id(n) as id,n LIMIT 1", name=name)

    @staticmethod
    def _create_manufacturer(tx, manufacturer):
        tx.run("CREATE (n:Manufacturer {name: $name}) ", name=manufacturer["name"])

    @staticmethod
    def _create_relation(tx, manufacturer):
        if manufacturer["parent"] is None or manufacturer["parent"] == "":
            return

        tx.run(
            "MATCH (d1:Manufacturer),(d2:Manufacturer) "
            "WHERE d1.name = $parent AND d2.name = $manufacturer_name "
            "CREATE (d2) - [pc:WORKSFOR {}] -> (d1)", parent=manufacturer["parent"], manufacturer_name
            =manufacturer["name"]
        )
