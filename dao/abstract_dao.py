class AbstractDao:

    def __init__(self, driver):
        self.driver = driver

    def close(self):
        self.driver.close()

    def handle_single_result(self, result):
        if result is None:
            return None
        result = {}
        for k, v in result.items():
            result[k] = v
        # result["_id"] = result["id"]
        return result
