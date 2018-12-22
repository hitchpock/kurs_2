import pytest
from class_bot import parsing_string


def test_bot():
    dct = parsing_string('dfhvkdf', 123, '',
                         {"action": "", "additional": "", "context_action": "", "speech": "", "default": ""})
    assert dct == {"action": "", "additional": "", "context_action": "", "speech": "", "default": "1"}
