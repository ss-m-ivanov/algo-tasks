import unittest
from unittest.mock import patch

from tasks_nazar import task_86_a
from tasks_nazar import task_86_b

class TestAlgo(unittest.TestCase):
    def test_task86_a(self):
        expected_answer = 2
        expected_input = str(10)
        with patch('builtins.input', return_value=expected_input) as _raw_input:
            self.assertEqual(task_86_a(), expected_answer)

    def test_task86_b(self):
        expected_answer = 15
        expected_input = str(12345)
        with patch('builtins.input', return_value=expected_input) as _raw_input:
            self.assertEqual(task_86_b(), expected_answer)
