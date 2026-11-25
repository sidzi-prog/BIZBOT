import uuid

import pytest

from bizbot.business import Business


def test_business():
    business = Business("sidzi barber shop", "barber")
    assert business.business_type == "barber"
    assert business.name == "sidzi barber shop"
    assert isinstance(business.id, str)
    assert uuid.UUID(business.id)
    assert business.is_active is False


def test_activate():
    business = Business("sidzi barber shop", "barber")
    business.activate()
    assert business.is_active is True


def test_deacrivate():
    business = Business("sidzi barber shop", "barber")
    business.activate()
    business.deactivate()
    assert business.is_active is False


def test_whitespace_name():
    with pytest.raises(ValueError):
        Business("   ", "barber")


def test_int_name():
    with pytest.raises(ValueError):
        Business(123, "barber")


def test_nothing_name():
    with pytest.raises(ValueError):
        Business("", "barber")


def test_whitespace_business_type():
    with pytest.raises(ValueError):
        Business("sidzi barber shop", "    ")


def test_init_business_type():
    with pytest.raises(ValueError):
        Business("sidzi barber shop", 123)


def test_nothing_business_type():
    with pytest.raises(ValueError):
        Business("sidzi barber shop", "")


def test_strip_inputs():
    business = Business("  sidzi barber shop   ", "   barber   ")
    assert business.name == "sidzi barber shop"
    assert business.business_type == "barber"
