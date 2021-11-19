import string
from numpy.random import default_rng
rng = default_rng()

def generate_random_password(length=12):

    output = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    rng.shuffle(output)
    output = rng.choice(output, length)
    rng.shuffle(output)
    output = "".join(output)

    return output

