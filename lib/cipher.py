import bcrypt

def gen_hash(text: str):
    bytes = str(text).encode('utf-8')
    salt = bcrypt.gensalt()
    
    return bcrypt.hashpw(bytes, salt)

def check_hash(text: str, hash: str):
    bytes = str(text).encode('utf-8')
    
    return bcrypt.checkpw(bytes, hash)