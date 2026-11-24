from bizbot.business import Business

import pytest

import uuid

def test_business():
    business= Business("barber")
    assert business.business_type == "barber"
    assert isinstance(business.id , str)
    assert uuid.UUID(business.id)
    assert business.is_active is False
def test_activate():
    business= Business("barber")
    business.activate()
    assert business.is_active is True
def test_whitespace():
    with pytest.raises(ValueError):
        business= Business("   ")
def test_int():
    with pytest.raises(ValueError):
        business= Business(123)
def test_nothing():
    with pytest.raises(ValueError):
        business= Business("")
