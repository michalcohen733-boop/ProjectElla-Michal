import hashlib
class Encoder:

    def calculate_hash_value(self, value):
        hash_value = hashlib.md5(value).hexdigest()
        # print(hash_value)
        return hash_value

