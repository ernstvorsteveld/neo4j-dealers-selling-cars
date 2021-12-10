from neo4j import GraphDatabase


class CreateDealers:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def __del__(self):
        self.close()

    def create(self, name, level, parent):
        with self.driver.session() as session:
            session.write_transaction(self._create_dealer, name, level)
            session.write_transaction(self._create_relation, name, parent)

    @staticmethod
    def _create_dealer(tx, name, level):
        if level == "TopLevel":
            tx.run("CREATE (n:Dealer:TopLevel {name: $name}) ", name=name)
        if level == "SubLevel":
            tx.run("CREATE (n:Dealer:SubLevel {name: $name}) ", name=name)

    @staticmethod
    def _create_relation(tx, dealer, parent):
        if parent is None or parent == "":
            return

        tx.run(
            "MATCH (d1:Dealer),(d2:Dealer) "
            "WHERE d1.name = $parent AND d2.name = $dealer "
            "CREATE (d2) - [pc:WORKSFOR {}] -> (d1)", parent=parent, dealer=dealer
        )
