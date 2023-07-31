"""
we should test the whole class or function fields toghether not one by one field
in case of adding a new field or attribute, the test should fail

"""

import unittest


def get_fruits():
    list = ['banana', 'apple', 'orange']
    return list


class TestMathOperations(unittest.TestCase):
    def test_aget_fruits(self):
        result = ['banana', 'apple', 'orange']
        func_result = get_fruits()
        self.assertEqual(func_result, get_fruits())
