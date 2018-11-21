# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function

import pkg_resources
from pathlib import Path

JS_GRAMMAR_PATH = Path(pkg_resources.resource_filename(__name__, 'js.ebnf'))
