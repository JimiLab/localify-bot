from hashlib import sha256
from config import BACKEND_TOKEN


def is_authenticated(auth):
    if auth is not None:
        auth = auth.decode('UTF-8')
        auth = auth.replace('Bearer ', '')
        auth = auth.strip().encode('UTF-8')
        if sha256(auth).hexdigest() == BACKEND_TOKEN:
            return True

    return False
