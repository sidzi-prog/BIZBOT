import uuid

import pytest

from bizbot.exceptions.domain import InvalidUserLanguageError, InvalidUserNameError
from bizbot.user import User


def test_user():
    user1 = User("sidzi", "fa")
    assert user1.full_name == "sidzi"
    assert isinstance(user1.id, str)
    assert uuid.UUID(user1.id)
    assert user1.is_active is True
    assert user1.language == "fa"


def test_deactive():
    user1 = User("sidzi", "fa")
    user1.deactivate()
    assert user1.is_active is False


def test_active():
    user1 = User("sidzi", "fa")
    user1.deactivate()
    user1.activate()
    assert user1.is_active is True


def test_fa_language():
    user1 = User("sidzi", "fa")
    assert user1.language == "fa"


def test_en_language():
    user1 = User("sidzi", "en")
    assert user1.language == "en"


def test_strip_name():
    user1 = User("  sidzi  ", "en")
    assert user1.full_name == "sidzi"


def test_whitespace():
    with pytest.raises(InvalidUserNameError):
        User("   ", "fa")


def test_int():
    with pytest.raises(InvalidUserNameError):
        User(123, "fa")


def test_nothing():
    with pytest.raises(InvalidUserNameError):
        User("", "fa")


def test_invalid_language():
    with pytest.raises(InvalidUserLanguageError):
        User("sidzi", "de")
