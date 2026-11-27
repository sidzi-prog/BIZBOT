from abc import ABC, abstractmethod


class DomainError(Exception, ABC):
    def __new__(cls, *args):
        if cls.__abstractmethods__:
            raise TypeError

        return Exception.__new__(cls, *args)

    @classmethod
    @abstractmethod
    def get_code(cls): ...


class InvalidBusinessNameError(DomainError):
    @classmethod
    def get_code(cls):
        return "invalid_business_name"


class InvalidBusinessTypeError(DomainError):
    @classmethod
    def get_code(cls):
        return "invalid_business_type"


class InvalidUserNameError(DomainError):
    @classmethod
    def get_code(cls):
        return "invalid_user_name"


class InvalidUserLanguageError(DomainError):
    @classmethod
    def get_code(cls):
        return "invalid_user_language"
