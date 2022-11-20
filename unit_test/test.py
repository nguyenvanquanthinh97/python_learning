import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('run before each test case function')

    def test_to_do(self):
        param = 10
        result = main.do_stuff(param)
        self.assertEqual(result, 15)

    def test_to_do2(self):
        param = 'sdlfjaslkdf'
        result = main.do_stuff(param)
        self.assertIsInstance(result, ValueError)

    def test_to_do3(self):
        param = None
        result = main.do_stuff(param)
        self.assertEqual(result, "Input a number")

    def test_to_do4(self):
        param = ""
        result = main.do_stuff(param)
        self.assertEqual(result, "Input a number")

    def test_to_do5(self):
        param = 0
        result = main.do_stuff(param)
        self.assertEqual(result, 5)

    def tearDown(self):
        print('run after each test case function')


if __name__ == '__main__':
    unittest.main()
