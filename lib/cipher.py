import bcrypt

class Hashing:
    def gen_hash(text):
        bytes = str(text).encode('utf-8')
        salt = bcrypt.gensalt()
        
        return bcrypt.hashpw(bytes, salt)

    def check_hash(text, hash):
        bytes = str(text).encode('utf-8')
        
        return bcrypt.checkpw(bytes, hash)