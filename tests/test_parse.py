# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function

import pytest

from tatsu.exceptions import TatSuException

import bojs
from .data import data_paths


testdata = data_paths()


@pytest.fixture()
def parser():
    return bojs.parser()


@pytest.mark.parametrize('filepath', testdata)
def test_parse(parser, filepath):
    with filepath.open() as f:
        code = f.read()
    try:
        parser.parse(code)
    except TatSuException as e:
        pytest.fail('%s on %s', str(e), filepath)
