from dao.abstract_dao import AbstractDao


class DealerDao(AbstractDao):

    def create(self, dealer):
        with self.driver.get().session() as session:
            session.write_transaction(self._create_dealer, dealer)
            session.write_transaction(self._create_relation, dealer)

    def get_by_name(self, name):
        with self.driver.get().session() as session:
            data = session.read_transaction(self._get_by_name, name)
            return self._handle_single_result(data)

    @staticmethod
    def _get_by_name(tx, name):
        return tx.run("MATCH (n:Dealer) WHERE (n.name=$name) return id(n) as id,n LIMIT 1", name=name).single()

    @staticmethod
    def _create_dealer(tx, dealer):
        if dealer["level"] == "TopLevel":
            tx.run("CREATE (n:Dealer:TopLevel {name: $name}) ", name=dealer["dealer"])
        if dealer["level"] == "SubLevel":
            tx.run("CREATE (n:Dealer:SubLevel {name: $name}) ", name=dealer["dealer"])

    @staticmethod
    def _create_relation(tx, dealer):
        if dealer["parent"] is None or dealer["parent"] == "":
            return

        tx.run(
            "MATCH (d1:Dealer),(d2:Dealer) "
            "WHERE d1.name = $parent AND d2.name = $dealer_name "
            "CREATE (d2) - [pc:WORKSFOR {}] -> (d1)", parent=dealer["parent"], dealer_name
            =dealer["dealer"]
        )
