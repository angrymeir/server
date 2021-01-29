import sys
sys.path.append('../')
from etebase_server.utils import get_secret_from_file

path = 'secret.txt'


def write_to_file(path):
    secret_key = "asdfakshjdfaksjdhf"
    with open(path, 'w') as f:
        f.write(secret_key)
    return secret_key


def test_secret_from_file_success():
    assert write_to_file(path) == get_secret_from_file(path)


def test_secret_from_file_fail():
    assert write_to_file(path) != get_secret_from_file(path) 
