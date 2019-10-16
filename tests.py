import unittest
from unittest.mock import patch

from tasks_nazar import task_86_a
from tasks_nazar import task_86_b
from tasks_nazar import task330


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

    def test_330_task(self):
        expect_input = 6
        expect_answer = [0]

        with patch('builtins.input', return_value=expect_input) as _raw_input:
            self.assertEqual(task330(), expect_answer)

    def test_second_for_330(self):
        # должен получить все совершонные числы меньше 8
        with patch('builtins.input', return_value=8) as _raw_input:
            self.assertEqual(task330(), [0, 6])