"""Find duplicate files on the file system.

Write a function duplicate_files() that takes a single argument of a directory
path (as a string) and returns a list of lists of duplicate file paths.

Example:

>>> duplicate_files('foo/bar')
[
    ['foo/bar/picture_1.jpg', 'foo/bar/picture_1_copy.jpg'],
    ['foo/bar/readme.txt', 'foo/bar/readme1.txt', 'foo/bar/readme2.txt'],
]

TIP: Use os.walk to walk the directory tree.
TIP: Use hashlib to create a hash of each file, if the hash is the same then
the files are to a small degree of uncertainty.

STRETCH: No modify the code so that it only looks at files specified by the
user. For example duplicate_files('foo/bar', '*.py')
TIP: Look at modules glob and fnmatch

STRETCH: Make it a full command line tool by allowing the user to specify
command line options. Example from the command line:
$ python DuplicateFiles.py --match="*.py" foo/bar
TIP: See the argparse module for specifying and processing command line
arguments.
"""


import os
import sys
import hashlib
import collections
import pprint
import cStringIO

import pytest
import mock

def duplicate_files(path):
    hash_dict = collections.defaultdict(list)
    for root, _dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            with open(file_path) as f:
                contents = f.read()
                hash_value = hashlib.sha1(contents).hexdigest()
                hash_dict[hash_value].append(file_path)
    return [v for v in hash_dict.values() if len(v) > 1]


def test_duplicate_files():
    with mock.patch('os.walk') as mock_walk:
        mock_walk.return_value = [
            ('/foo', ('bar',), ('A', 'B', 'C', 'D')),
        ]
        file_contents = ['alpha', 'bravo', 'bravo', 'delta']
        with mock.patch('__builtin__.open', create=True) as mock_open:
            mock_open.return_value = mock.MagicMock(spec=file)
            m_file = mock_open.return_value.__enter__.return_value
            m_file.read.side_effect = lambda: file_contents.pop(0)
            result = duplicate_files('path')
            assert result == [['/foo/B', '/foo/C']]


def main():
    pprint.pprint(duplicate_files(sys.argv[1]))

if __name__ == "__main__":
    main()
