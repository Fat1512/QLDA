import unittest


class TestLogin(unittest.TestCase):
    def test_true(self):
        self.assertTrue("admin", "123")

    def test_false(self):
        self.assertTrue("admin", 456)


if __name__ == '__main__':
    unittest.main()
