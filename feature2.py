import hashlib
class Encoder:

    def __init__(self, value):
        self.value = value
    def calculate_hash_value(self):
        hash_value = hashlib.md5(self.value).hexdigest()
        print(hash_value)
        return hash_value
    def get_file_content 
