import hashlib
import os

path = os.path.abspath('countries_new.txt')


def hashing(line):
    yield hashlib.md5(line.encode()).hexdigest()


with open(path) as file:
    for one_line in file:
        print(*hashing(one_line))