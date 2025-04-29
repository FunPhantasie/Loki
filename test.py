import os
import random
import string
def zufallsname():
    return ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 9)))
print(zufallsname())