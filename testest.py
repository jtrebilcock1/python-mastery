import unittest
import test


class Testtest(unittest.TestCase):

	def test_add(self):#this is just one test
		self.assertEqual(test.add(10, 5), 15)
		self.assertEqual(test.add(-1, 1), 0)
		self.assertEqual(test.add(-1, -1), -2)

	def test_subtract(self):
		self.assertEqual(test.subtract(10, 5), 5)
		self.assertEqual(test.subtract(-1, 1), -2)
		self.assertEqual(test.subtract(-1, -1), 0)

	def test_multiply(self):
		self.assertEqual(test.multiply(10, 5), 50)
		self.assertEqual(test.multiply(-1, 1), -1)
		self.assertEqual(test.multiply(-1, -1), 1)

	def test_divide(self):
		self.assertEqual(test.divide(10, 5), 2)
		self.assertEqual(test.divide(-1, 1), -1)
		self.assertEqual(test.divide(-1, -1), 1)
		self.assertEqual(test.divide(5, 2), 2.5)

		with self.assertRaises(ValueError): #arg is expected error. so if arg was suntaxerror this test would fail
			test.divide(10, 0)


if __name__ == '__main__':
	unittest.main()