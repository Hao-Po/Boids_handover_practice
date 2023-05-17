import unittest
import sys
from io import StringIO
from lesson_3_loop import loop_practice

lp = loop_practice()


class TestClass(unittest.TestCase):
    def test_simple_while_loop(self):
        answer = lp.simple_while_loop(10)
        self.assertEqual(answer, 45)

        answer = lp.simple_while_loop(100)
        self.assertEqual(answer, 4950)

        answer = lp.simple_while_loop(2000)
        self.assertEqual(answer, 1999000)

    def test_simple_for_loop(self):
        answer = lp.simple_for_loop(10)
        self.assertEqual(answer, 45)

        answer = lp.simple_for_loop(100)
        self.assertEqual(answer, 4950)

        answer = lp.simple_for_loop(2000)
        self.assertEqual(answer, 1999000)

    def test_list_for_loop(self):
        input_list = [2, 5, 7]
        answer = lp.list_for_loop(input_list)
        self.assertEqual(answer, 14)

        input_list = [11, 3, 77, 44, 56]
        answer = lp.list_for_loop(input_list)
        self.assertEqual(answer, 191)

    def test_dict_for_loop(self):
        input_dict = {
            "Tom": 10,
            "Ken": 90,
            "Ruby": 77
        }
        stdout = sys.stdout
        sys.stdout = StringIO()
        lp.dict_for_loop(input_dict)
        output = sys.stdout.getvalue()
        sys.stdout = stdout
        self.assertEqual(output, "Tom, 10\nKen, 90\nRuby, 77\n")


if __name__ == '__main__':
    unittest.main()
