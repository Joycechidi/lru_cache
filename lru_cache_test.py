import unittest


class TestProgram(unittest.TestCase):
    def test_case_one(self):
        lru_cache = program.LRUCache(10)
        lru_cache.put_key_value("first", 10)
        lru_cache.put_key_value("second", 11)
        lru_cache.put_key_value("third", 12)
        self.assertEqual(lru_cache.get_value_from_key("first")
