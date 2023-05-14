import hashlib
import time

def hash_string(string):
    """Compute SHA-256 hash of a string"""
    hash_object = hashlib.sha256(string.encode('utf-8'))
    return hash_object.hexdigest()

string = "abcdefghijklmnopqrstuvwxyz" * 100000

start_time = time.time()

while True:
    hash_string(string)

    elapsed_time = time.time() - start_time
    if elapsed_time >= 60:
        break
