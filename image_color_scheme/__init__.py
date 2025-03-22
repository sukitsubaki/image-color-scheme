"""
image-color-scheme
~~~~~~~~~~~~~~~~~

A lightweight library to extract dominant colors from images and create color palettes.

:copyright: (c) 2025 Suki Tsubaki
:license: MIT, see LICENSE for more details.
"""

__version__ = "0.2.1"

from .color_extractor import extract_colors, Color
from .palette_generator import generate_palette, PaletteType

__all__ = [
    "extract_colors", 
    "generate_palette", 
    "Color", 
    "PaletteType"
]
