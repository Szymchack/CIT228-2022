import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Make an employee to use in tests."""
        self.cathyann = Employee('cathyann', 'johnson', 65_000)

    def test_give_default_raise(self):
        self.cathyann.give_raise()
        self.assertEqual(self.cathyann.salary, 70000)

    def test_give_custom_raise(self):
        self.cathyann.give_raise(10000)
        self.assertEqual(self.cathyann.salary, 75000)

if __name__ == '__main__':
    unittest.main()