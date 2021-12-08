# -*- coding: utf-8 -*-

"""
GIF raw reading Library.

Gifraw is a python GIF reading library.
It is made for adding some feature to PILLOW/imageio palette problem.

by bongdang
"""

from .__consts__ import VERSION, DESCRIPTION, AUTHOR

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())

from .mainclass import GifRaw


def __repr__():
    return f"{DESCRIPTION} : Version ({VERSION}) : by {AUTHOR}"
