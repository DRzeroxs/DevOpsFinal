import unittest

class TestHolaMundo(unittest.TestCase):
    def test_hola_mundo(self):
        with open("index.html", "r") as file:
            content = file.read()
        self.assertIn("Hola Mundo", content)

if __name__ == "__main__":
    unittest.main()
