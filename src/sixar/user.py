import uuid

from sixar.exceptions.domain import InvalidUserLanguageError, InvalidUserNameError


class User:
    def __init__(self, full_name, language):
        if not isinstance(full_name, str) or not full_name.strip():
            raise InvalidUserNameError

        if language not in ("fa", "en"):
            raise InvalidUserLanguageError

        self.full_name = full_name.strip()
        self.id = str(uuid.uuid4())
        self.is_active = True
        self.language = language

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
