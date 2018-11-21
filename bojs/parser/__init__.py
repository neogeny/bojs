# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function

from .js_parser import JavaScriptParser
from .js_model import JavaScriptModelBuilderSemantics


__parser = None


def parser():
    return JavaScriptParser(semantics=JavaScriptModelBuilderSemantics())
