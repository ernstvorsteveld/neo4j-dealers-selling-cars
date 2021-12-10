from neo4j import GraphDatabase


class CreateDealers:

    def __init__(self, driver):
        self.driver = driver

    def create(self, dealer):
        with self.driver.get().session() as session:
            session.write_transaction(self._create_dealer, dealer)
            session.write_transaction(self._create_relation, dealer)

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
