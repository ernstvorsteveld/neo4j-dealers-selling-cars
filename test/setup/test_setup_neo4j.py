import test.test_dao as testdao
import setup.setup_neo4j as sn


class TestCarDao(testdao.TestDao):

    def setUp(self):
        self.driver()

    def test_configure(self):
        pass
