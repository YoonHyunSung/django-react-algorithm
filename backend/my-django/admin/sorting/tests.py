from django.test import TestCase
import unittest
# Create your tests here.
# import sys
# sys.path.append('/admin/sorting')
from admin.sorting.models import MySum, Palindrome


class TestPalindrome(unittest.TestCase):
    def test_str_to_list(self):
        instance = Palindrome()
        instance.input_string = 'abcd'
        res1 = instance.isPalindrome()
        self.assertEqual(res1, {'RESULT': False})

    def test_reverse_string(self):
        instance = Palindrome()
        instance.input_string = 'abcd'
        res = instance.reverse_string()
        self.assertEqual(res, ['d', 'c', 'b', 'a'])

class TestMySum(unittest.TestCase):

    def test_one_to_ten_sum_1(self):
        instance = MySum()
        instance.start_number = 1
        instance.end_number = 11
        res = instance.one_to_ten_sum_2()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)

if __name__ == '__main__':
    unittest.main()