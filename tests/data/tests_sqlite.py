import unittest
import os
from packages.data.sqlite import SQLiteHandler

class TestSQLiteHandler(unittest.TestCase):
    DB_PATH = "test_database.db"

    @classmethod
    def setUpClass(cls):
        """Set up the test database and SQLiteHandler instance."""
        cls.db = SQLiteHandler(cls.DB_PATH)
        cls.db.create_table("users", ["id INTEGER PRIMARY KEY", "name TEXT", "age INTEGER"])

    @classmethod
    def tearDownClass(cls):
        """Close the database connection and remove the test database."""
        cls.db.close()
        os.remove(cls.DB_PATH)

    def test_create(self):
        """Test inserting a new record."""
        user_id = self.db.create("users", {"name": "Alice", "age": 25})
        self.assertIsInstance(user_id, int)  # Check if ID is an integer

    def test_read(self):
        """Test reading records from the table."""
        users = self.db.read("users")
        self.assertGreater(len(users), 0)  # Ensure there's at least one user

    def test_update(self):
        """Test updating a record."""
        rows_updated = self.db.update("users", {"age": 26}, {"name": "Alice"})
        self.assertEqual(rows_updated, 1)

    def test_get_single_value(self):
        """Test retrieving a single value."""
        age = self.db.get_single_value("users", "age", {"name": "Alice"})
        self.assertEqual(age, 26)  # Check if update worked

    def test_delete(self):
        """Test deleting a record."""
        rows_deleted = self.db.delete("users", {"name": "Alice"})
        self.assertEqual(rows_deleted, 1)

if __name__ == "__main__":
    unittest.main()
