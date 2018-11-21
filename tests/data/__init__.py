# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function

import pkg_resources
from pathlib import Path


DATA_PATH = Path(pkg_resources.resource_filename(__name__, ''))


def data_paths():
    return list(DATA_PATH.glob('**/*.js'))
