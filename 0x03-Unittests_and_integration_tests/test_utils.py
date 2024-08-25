#!/usr/bin/env python3

"""
UnitTest utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import (access_nested_map)


class TestAccessNestedMap(unittest.TestCase):
    
    """
    Class TestAccessNestedMap
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that the method that returns what is supposed to
        """
        
        