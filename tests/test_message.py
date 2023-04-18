import pytest
from devchat.message import Message

def test_valid_message_creation():
    message = Message(role="user", content="Hello, World!")
    assert message.role == "user"
    assert message.content == "Hello, World!"
    assert message.name is None

def test_valid_message():
    message = Message("user", "Hello, World!", "John_Doe")
    assert message.to_dict() == {"role": "user", "content": "Hello, World!", "name": "John_Doe"}

def test_invalid_role():
    with pytest.raises(ValueError):
        Message("invalid_role", "Hello, World!")

def test_none_content():
    with pytest.raises(ValueError):
        Message(role="user", content=None)

def test_empty_content():
    with pytest.raises(ValueError):
        Message("user", "")

def test_blank_content():
    with pytest.raises(ValueError):
        Message("user", "  ")

def test_none_content():
    with pytest.raises(ValueError):
        Message("user", None)

def test_invalid_name():
    with pytest.raises(ValueError):
        Message("user", "Hello, World!", "Invalid@Name")

def test_empty_name():
    with pytest.raises(ValueError):
        Message("user", "Hello, World!", "")

def test_blank_name():
    with pytest.raises(ValueError):
        Message("user", "Hello, World!", "  ")

def test_tab_content():
    with pytest.raises(ValueError):
        Message(role="user", content="\t")

def test_none_name():
    message = Message("user", "Hello, World!", None)
    assert message.to_dict() == {"role": "user", "content": "Hello, World!"}
