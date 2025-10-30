import hashlib
class MD5HASH:
#MD5
    def calculate_hash_value(self, value):
        hash_value = hashlib.md5(value).hexdigest()
        return hash_value

class SHA1HASH:
#SHA1
    def calculate_hash_value(self,value):
        hash_value = hashlib.sha1(value).hexdigest()
        return hash_value

class SHA256HASH:
#SHA256
    def calculate_hash_value(self,value):
        hash_value = hashlib.sha256(value).hexdigest()
        return hash_value

