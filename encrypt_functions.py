import hmac
import random
import string

SECRET = "lizbot"

def hash_str(s):
    return hmac.new(SECRET,s).hexdigest()

def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val

def make_salt(n=5):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n))

def make_hash(name,pw,salt=None):
    if not salt:
        salt = make_salt()
    return "{}|{}".format(hash_str(name+pw+salt),salt)

def valid_pw(name,pw,h):
    salt = h.split('|')[1]
    return make_hash(name,pw,salt) == h

if __name__ == "__main__":
    pass
