import pytest

from sixar.exceptions.domain import (
    DomainError,
    InvalidBusinessNameError,
    InvalidBusinessTypeError,
    InvalidUserLanguageError,
    InvalidUserNameError,
)


def test_invalid_business_name_error_code():
    assert InvalidBusinessNameError.get_code() == "invalid_business_name"


def test_invalid_business_name_error_code_from_instance():
    error = InvalidBusinessNameError()
    assert error.get_code() == "invalid_business_name"


def test_invalid_business_type_error_code():
    assert InvalidBusinessTypeError.get_code() == "invalid_business_type"


def test_invalid_business_type_error_code_from_instance():
    error = InvalidBusinessTypeError()
    assert error.get_code() == "invalid_business_type"


def test_invalid_user_name_error_code():
    assert InvalidUserNameError.get_code() == "invalid_user_name"


def test_invalid_user_name_error_code_from_instance():
    error = InvalidUserNameError()
    assert error.get_code() == "invalid_user_name"


def test_invalid_user_language_error_code():
    assert InvalidUserLanguageError.get_code() == "invalid_user_language"


def test_invalid_user_language_error_code_from_instance():
    error = InvalidUserLanguageError()
    assert error.get_code() == "invalid_user_language"


def test_error_codes_are_unique():
    error1 = InvalidBusinessNameError.get_code()
    error2 = InvalidBusinessTypeError.get_code()
    error3 = InvalidUserNameError.get_code()
    error4 = InvalidUserLanguageError.get_code()
    error_codes = {error1, error2, error3, error4}
    assert len(error_codes) == 4


def test_abstract_domain_error_class():
    with pytest.raises(TypeError):
        DomainError()


def test_subclass_from_domain_error():
    assert issubclass(InvalidUserLanguageError, DomainError)
    assert issubclass(InvalidBusinessNameError, DomainError)
    assert issubclass(InvalidBusinessTypeError, DomainError)
    assert issubclass(InvalidUserNameError, DomainError)


def test_domain_error_is_exception():
    assert issubclass(InvalidUserNameError, Exception)
    assert issubclass(InvalidUserLanguageError, Exception)
    assert issubclass(InvalidBusinessTypeError, Exception)
    assert issubclass(InvalidBusinessNameError, Exception)


def test_exception_can_be_raised_and_caught():
    with pytest.raises(InvalidUserNameError):
        raise InvalidUserNameError()


def test_domain_error_preserves_message():
    error = InvalidUserNameError("Invalid user name")

    assert str(error) == "Invalid user name"
    assert error.args == ("Invalid user name",)
