# -*- coding: utf-8 -*-
from os import path
from os import remove
from os import sep
from shutil import rmtree

import pytest

from pupy.savings_n_loads import ljasm
from pupy.savings_n_loads import ljson
from pupy.savings_n_loads import load_jasm
from pupy.savings_n_loads import lpak
from pupy.savings_n_loads import lstr
from pupy.savings_n_loads import lstring
from pupy.savings_n_loads import ltoml
from pupy.savings_n_loads import lyaml
from pupy.savings_n_loads import safepath
from pupy.savings_n_loads import save_jasm
from pupy.savings_n_loads import savings
from pupy.savings_n_loads import sjasm
from pupy.savings_n_loads import sjson
from pupy.savings_n_loads import spak
from pupy.savings_n_loads import sstr
from pupy.savings_n_loads import sstring
from pupy.savings_n_loads import stoml
from pupy.savings_n_loads import syaml
from pupy.sh import touch

JASM_DICT = {"Jason": ["Green", "Berg"], "Jasm": ["Grundle", "Bug"]}


@pytest.mark.parametrize(
    "save_funk,load_funk", [[sstring, lstring], [savings, lstring], [sstr, lstr]]
)
def test_savings_n_loads_methods(save_funk, load_funk):
    fp = "somefile.txt"
    string = "12345\n12345"
    save_funk(fp, string)
    s = load_funk(fp)
    assert s == string
    remove(fp)


@pytest.mark.parametrize(
    "save_funk,load_funk",
    [
        [save_jasm, load_jasm],
        [sjson, ljson],
        [sjasm, ljasm],
        [spak, lpak],
        [stoml, ltoml],
        [syaml, lyaml],
    ],
)
def test_ljson_n_sjson(save_funk: callable, load_funk: callable):
    """

    """
    fp = safepath("jasm_dict.json")
    save_funk(fp, JASM_DICT)
    loaded_data = load_funk(fp)
    assert loaded_data == JASM_DICT
    remove(fp)


@pytest.mark.parametrize(
    "save_funk,load_funk",
    [
        [save_jasm, load_jasm],
        [sjson, ljson],
        [sjasm, ljasm],
        [spak, lpak],
        [stoml, ltoml],
        [syaml, lyaml],
    ],
)
def test_ljson_n_sjson_safe_save(save_funk: callable, load_funk: callable):
    """

    """
    fp = "jasm_dict_safe_save.json"
    save_funk(fp, JASM_DICT)
    fp2 = safepath(fp)
    save_funk(fp2, JASM_DICT)
    loaded_data = load_funk("jasm_dict_safe_save.json")
    assert loaded_data == JASM_DICT
    remove(fp)
    loaded_data = load_funk(fp2)
    assert loaded_data == JASM_DICT
    remove(fp2)


@pytest.mark.parametrize(
    "save_funk,load_funk", [[save_jasm, load_jasm], [sjson, ljson], [sjasm, ljasm]]
)
def test_ljson_n_sjson_min(save_funk: callable, load_funk: callable):
    """

    """
    fp = safepath("jasm_dict.json")
    save_funk(fp, JASM_DICT, minify=True)
    loaded_data = load_funk(fp)
    assert loaded_data == JASM_DICT
    remove(fp)


@pytest.mark.parametrize(
    "fdpath",
    [
        "file.txt",
        path.join("dir", "file.txt"),
        path.join("dir1", "dir2", "file.txt"),
        path.join("dir1", "dir2", "dir3", "file.txt"),
        path.join("dir1", "dir2", "dir3", "dir4", "file.txt"),
    ],
)
def test_touch(fdpath):
    assert not path.exists(fdpath)
    touch(fdpath)
    assert path.exists(fdpath)

    root = fdpath.split(sep)[0]
    if path.isdir(root):
        rmtree(root)
    elif path.isfile(root):
        remove(root)


def test_safepath():
    filepath = "afile.txt"
    d = safepath(filepath)
    assert d == filepath
    savings(filepath, "1234567")
    d = safepath(filepath)
    assert d != filepath
    remove(filepath)
