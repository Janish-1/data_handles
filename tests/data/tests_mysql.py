import unittest
from packages.data.mysql import MySQLSocketHandler

class TestMySQLSocketHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mysql_handler = MySQLSocketHandler("127.0.0.1", 3306)
        cls.mysql_handler.create_table("test_users", ["id INT PRIMARY KEY", "name VARCHAR(100)"])
    
    def test_insert(self):
        result = self.mysql_handler.insert("test_users", {"id": 1, "name": "Alice"})
        self.assertIsNotNone(result)
    
    def test_read_one(self):
        self.mysql_handler.insert("test_users", {"id": 2, "name": "Bob"})
        result = self.mysql_handler.read_one("test_users", {"id": 2})
        self.assertIn(b"Bob", result)
    
    def test_read_all(self):
        result = self.mysql_handler.read_all("test_users")
        self.assertTrue(len(result) > 0)
    
    def test_update(self):
        self.mysql_handler.insert("test_users", {"id": 3, "name": "Charlie"})
        self.mysql_handler.update("test_users", {"name": "Charlie Updated"}, {"id": 3})
        result = self.mysql_handler.read_one("test_users", {"id": 3})
        self.assertIn(b"Charlie Updated", result)
    
    def test_delete(self):
        self.mysql_handler.insert("test_users", {"id": 4, "name": "David"})
        self.mysql_handler.delete("test_users", {"id": 4})
        result = self.mysql_handler.read_one("test_users", {"id": 4})
        self.assertNotIn(b"David", result)
    
    @classmethod
    def tearDownClass(cls):
        cls.mysql_handler.close()

if __name__ == "__main__":
    unittest.main()
