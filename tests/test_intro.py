from intro import __version__
import intro

from intro.__main__ import file_base
from os.path import dirname as osdirname, join as osjoin, exists


def test_version():
    assert __version__ == '0.1.0'


def test_if_file_exists():
    file_path = osjoin(osdirname(intro.__file__), file_base)
    is_file_exist = exists(file_path)
    assert is_file_exist
