import unittest
import mainTest1


class TestMain(unittest.TestCase):

    def setUp(self):
        print('About to test a function')

    def test_do_stuff(self):
        testparam = 10
        result = mainTest1.do_stuff(testparam)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        testparam = 'lolxd'
        result = mainTest1.do_stuff(testparam)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        testparam = None
        result = mainTest1.do_stuff(testparam)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        testparam = ''
        result = mainTest1.do_stuff(testparam)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff5(self):
        testparam = 0
        result = mainTest1.do_stuff(testparam)
        self.assertEqual(result, '0')

    def tearDown(self):
        print('Cleaning your mess!')


if __name__ == '__main__':
    unittest.main()
