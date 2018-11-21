# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function

import sys
from pathlib import Path
from . import parser


def main():
    filepath = Path(sys.argv[1])
    with filepath.open() as f:
        parser().parse(f.read(), trace=True, colorize=True)


if __name__ == '__main__':
    main()
