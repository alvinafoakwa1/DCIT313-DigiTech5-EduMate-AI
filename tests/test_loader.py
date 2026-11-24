import unittest
from src.data_loader import load_and_chunk_notes

class TestDataLoader(unittest.TestCase):
    def test_load_sample_notes(self):
        chunks = load_and_chunk_notes("data/sample_db_notes.txt")
        self.assertGreaterEqual(len(chunks), 3)
        self.assertIn("Normalization", chunks[0])

    def test_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            load_and_chunk_notes("data/non_existent.txt")

if __name__ == "__main__":
    unittest.main()
