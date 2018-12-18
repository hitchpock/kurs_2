import unittest
from class_bot import parsing_string


class TestBot(unittest.TestCase):
    def test_bot(self):
        dct = parsing_string('dfhvkdf', 123, '',
                             {"action": "", "additional": "", "context_action": "", "speech": "", "default": ""})
        self.assertEqual(dct, {"action": "", "additional": "", "context_action": "", "speech": "", "default": "1"})


if __name__ == '__main__':
    unittest.main()
