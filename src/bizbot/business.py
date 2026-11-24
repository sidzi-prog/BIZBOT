import uuid

class Business:
    def __init__(self, business_type):

        if isinstance(business_type, str) and business_type.strip():
            self.business_type= business_type
            self.id= str(uuid.uuid4())
            self.is_active= False
        else:
            raise ValueError("The business type is not valid")

    def activate(self):
        self.is_active= True
