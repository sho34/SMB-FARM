import os
from hashlib import sha256


class randomValueGen:
    # shared by instances 
    use_case_count = 0
    def __init__(self):
        self.value = os.urandom(8) * 2
        self.salt_value = sha256(self.value)

    def generate_random_id(self) -> str:
        return self.salt_value.hexdigest()