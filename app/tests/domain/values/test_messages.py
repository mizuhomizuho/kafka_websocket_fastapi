from datetime import datetime

import pytest

from domain.entities.messages import Message, Chat
from domain.exceptions.messages import TitleTooLongException
from domain.values.messages import Text, Title


def test_create_message_success_short_text():
    text: Text = Text('Meow')
    message: Message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_message_success_long_text():
    text: Text = Text('Meow' * 888)
    message: Message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_chat_success():
    title: Title = Title('Meow')
    chat: Chat = Chat(title=title)

    assert chat.title == title
    assert not chat.messages
    assert chat.created_at.date() == datetime.today().date()


def test_create_title_too_long():
    with pytest.raises(TitleTooLongException):
        Title('Meow' * 888 )


def test_add_chat_to_message():
    text: Text = Text('Meow')
    message: Message = Message(text=text)

    title: Title = Title('Meow')
    chat: Chat = Chat(title=title)

    chat.add_message(message)

    assert message in chat.messages