################
# wordTest
################


import unittest
import wordCount


class TestWordCount(unittest.TestCase):


	def test_type(self):
		print("If a there is an error from this test, the code is implemented correctly")
		with self.assertRaises(TypeError): wordCount.words()
		print("There is a Type Error ...")

	def test_correctness(self):
		answer = len(wordCount.words())
		expecteds = input("How many words do you expect to be counted in the above sentence: ")
		expected = int(expecteds)
		self.assertEqual(answer, expected)

	def test_negative(self):
		answer = len(wordCount.words())
		self.assertLess(0, answer)


if __name__ == '__main__':
	unittest.main()
