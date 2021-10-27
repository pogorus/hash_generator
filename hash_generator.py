import hashlib

def md5_hasher(string):
    hash = hashlib.md5(string.encode())
    return hash.hexdigest()

def hash_generator(path):
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            yield md5_hasher(line)
            line = f.readline()

for line in hash_generator('file.txt'):
    print(line)

