import uuid


class User:
    def __init__(self, full_name):
        if isinstance(full_name, str) and full_name.strip():
            self.full_name = full_name
            self.id = str(uuid.uuid4())
            self.is_active = True
        else:
            raise ValueError("Your full name is not valid")

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
