class DomainError(Exception):
    pass


class InvalidBusinessNameError(DomainError):
    pass


class InvalidBusinessTypeError(DomainError):
    pass


class InvalidUserNameError(DomainError):
    pass
