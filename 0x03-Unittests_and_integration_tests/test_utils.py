#!/usr/bin/env python3

"""
UnitTest utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import (access_nested_map, get_json)


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
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test that that method raises expected exception
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """
    def class TestGetJson(unittest.TestCase)
    """
    def test_get_json(self, test_url, test_payload):
        """
        Checks  get_json returns expected results
        """
