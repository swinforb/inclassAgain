	################
# palTest
################


import unittest
import palindrome


class TestPalindrome(unittest.TestCase):


	def test_type(self):
		print("If a there is an error from this test, the code is implemented correctly")
		with self.assertRaises(TypeError): palindrome.pal()
		print("There is a Type Error ...")

def test_equivalence(self):
		lengthOG = input("Please enter the word to test that the length is not changed: ")
		print("Now enter the same exact word again")
		this = len(lengthOG)
		that = len(palindrome.pal())
		self.assertTrue(this == that)

	def test_empty(self):
		length = len(palindrome.pal())
		self.assertNotEqual(length, 0)
		


if __name__ == '__main__':
	unittest.main()
