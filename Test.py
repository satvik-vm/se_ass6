#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from program import multiply

class TestSum(unittest.TestCase):
	def test_1(self):
		a_1 = 10
		b_1 = 10
		result = multiply(a_1, b_1)
		self.assertEqual(result, 100)
	
	def test_2(self):
		a_2 = 10
		b_2 = 5
		result = multiply(a_2, b_2)
		self.assertEqual(result, 50)

	def test_3(self):
		a_3 = 5
		b_3 = 5
		result = multiply(a_3, b_3)
		self.assertEqual(result, 25)

# 	def test_4(self):
# 		a_4 = 2
# 		b_4 = 5
# 		result = multiply(a_4, b_4)
# 		self.assertEqual(result, 20) 

# 	def test_5(self):
# 		a_5 = 5
# 		b_5 = 4
# 		result = multiply(a_5, b_5)
# 		self.assertEqual(result, 25)

if __name__ == '__main__':
	unittest.main()
