import unittest

#From the folder hello_world, import the function hello
from hello_world import hello
from string_compare import diff_count


class HelloWorldTest(unittest.TestCase):
  def test_say_hello(self):
    expected = "Hello World!"
    self.assertEqual(hello(), expected)


class StringCompareTest(unittest.TestCase):
  def test_identical_count(self):
    self.assertEqual(diff_count('GAGCCTACTAACGGGAT','CATCGTAATGACGGCCT'), 7 )

  def test_single_identical_count(self):
    self.assertEqual(diff_count('A','A'), 0 )

  def test_single_different_count(self):
    self.assertEqual(diff_count('B','A'), 1 )

  def test_empty_strings(self):
    self.assertEqual(diff_count('',''), 0 )    

  def test_different_length_string(self):
    with self.assertRaises(ValueError):
      diff_count('AG', 'GAGCC')

  def test_one_empty_string(self):
    with self.assertRaises(ValueError):
      diff_count('', 'GAGCC')    

if __name__ == "__main__":
  unittest.main() 