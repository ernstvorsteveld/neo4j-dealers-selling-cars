from database_accessor import DatabaseAccessor


class CreateManufacturer(DatabaseAccessor):

    def create(self, manufacturer):
        with self.driver.get().session() as session:
            session.write_transaction(self._create_manufacturer, manufacturer)
            session.write_transaction(self._create_relation, manufacturer)

    @staticmethod
    def _create_manufacturer(tx, dealer):
        None

    @staticmethod
    def _create_relation(tx, dealer):
        None
