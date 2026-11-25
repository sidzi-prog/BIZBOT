import uuid


class Business:
    def __init__(self, name, business_type):

        if not isinstance(name, str) or not name.strip():
            raise ValueError("the name not valid")
        if not isinstance(business_type, str) or not business_type.strip():
            raise ValueError("the business type is not valid")
        self.business_type = business_type.strip()
        self.name = name.strip()
        self.id = str(uuid.uuid4())
        self.is_active = False

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
