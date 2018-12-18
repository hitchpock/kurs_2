import unittest
from class_bot import Bot


class TestBot(unittest.TestCase):
    def test_bot(self):
        a = Bot(message=None, text='djnvfjd', bot=None)
        a.context = ""
        dct = a.create_dict()
        self.assertEqual(dct, {"action": "", "additional": "", "context_action": "", "speech": "", "default": "1"})


if __name__ == '__main__':
    unittest.main()
