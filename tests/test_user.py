from bizbot.user import User

import pytest

import uuid

def test_user():
    user1= User("sidzi")
    assert user1.full_name== "sidzi"
    assert isinstance(user1.id , str)
    assert uuid.UUID(user1.id)
    assert user1.is_active is True
def test_deactive():
    user1= User("sidzi")
    user1.deactivate()
    assert user1.is_active is False
def test_active():
    user1= User("sidzi")
    user1.deactivate()
    user1.activate()
    assert user1.is_active is True
def test_whitespace():
    with pytest.raises(ValueError):
        user1= User("   ")
def test_int():
    with pytest.raises(ValueError):
        user1= User(123)
def test_nothing():
    with pytest.raises(ValueError):
        user1= User("")
