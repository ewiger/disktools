import os
import random
import unittest
import tempfile
from sh import du
from disktools.disk_usage import get_size


def write_blob(filename, size=None):
    size = random.randint(1, 1000000)
    with open(filename, 'w+') as output:
        output.write(bytearray(os.urandom(size)))


def get_expected_size(path):
    '''Ground truth by gnu utils'''
    return du('-s', path).split()[:1]


class TestDiskUsage(unittest.TestCase):

    def setUp(self):
        self.root = tempfile.mkdtemp()
        # mock it up
        count = 10
        for num1 in range(1, count):
            path = os.path.join(self.root, str(num1))
            os.mkdir(path)
            subcount = random.randint(1, 5)
            for num2 in range(1, subcount):
                subpath = os.path.join(path, str(num2))
                write_blob(subpath)

    def test_get_size(self):
        expected_size = get_expected_size(self.root)
        size = get_size(self.root)
        self.assertEqual(size, expected_size)
