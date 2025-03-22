"""
Palette generation module for image-color-scheme.
"""

import colorsys
from enum import Enum
import numpy as np
from .color_extractor import Color


class PaletteType(Enum):
    """
    Types of color palettes that can be generated.
    """
    MONOCHROMATIC = "monochromatic"
    ANALOGOUS = "analogous"
    COMPLEMENTARY = "complementary"
    TRIADIC = "triadic"
    TETRADIC = "tetradic"
    

def generate_palette(colors, palette_type=PaletteType.MONOCHROMATIC, num_colors=5):
    """
    Generate a color palette based on the extracted colors.
    
    Args:
        colors (list): List of Color objects.
        palette_type (PaletteType): Type of palette to generate.
        num_colors (int): Number of colors in the palette.
        
    Returns:
        list: A list of Color objects making up the palette.
    """
    if not colors:
        raise ValueError("No colors provided")
    
    # Use the most dominant color (first in the list) as the base
    base_color = colors[0]
    
    if palette_type == PaletteType.MONOCHROMATIC:
        return _generate_monochromatic(base_color, num_colors)
    elif palette_type == PaletteType.ANALOGOUS:
        return _generate_analogous(base_color, num_colors)
    elif palette_type == PaletteType.COMPLEMENTARY:
        return _generate_complementary(base_color, num_colors)
    elif palette_type == PaletteType.TRIADIC:
        return _generate_triadic(base_color, num_colors)
    elif palette_type == PaletteType.TETRADIC:
        return _generate_tetradic(base_color, num_colors)
    else:
        raise ValueError(f"Unknown palette type: {palette_type}")


def _generate_monochromatic(base_color, num_colors):
    """Generate a monochromatic palette based on a single color."""
    h, s, v = base_color.hsv
    
    # Create variations by adjusting saturation and value
    palette = []
    for i in range(num_colors):
        # Vary both saturation and value
        new_s = max(0.1, min(1.0, s * (0.5 + i/num_colors)))
        new_v = max(0.2, min(1.0, v * (0.5 + i/num_colors)))
        
        # Convert back to RGB
        rgb = colorsys.hsv_to_rgb(h, new_s, new_v)
        rgb_255 = tuple(int(c * 255) for c in rgb)
        
        palette.append(Color(rgb_255))
    
    return palette


def _generate_analogous(base_color, num_colors):
    """Generate an analogous palette (colors adjacent on the color wheel)."""
    h, s, v = base_color.hsv
    
    # Create colors by shifting the hue slightly
    palette = []
    hue_shift = 0.05  # About 18 degrees on the color wheel
    
    for i in range(num_colors):
        # Shift the hue in both directions from the base
        shift = (i - num_colors // 2) * hue_shift
        new_h = (h + shift) % 1.0
        
        # Convert back to RGB
        rgb = colorsys.hsv_to_rgb(new_h, s, v)
        rgb_255 = tuple(int(c * 255) for c in rgb)
        
        palette.append(Color(rgb_255))
    
    return palette


def _generate_complementary(base_color, num_colors):
    """Generate a complementary palette (opposite colors on the color wheel)."""
    h, s, v = base_color.hsv
    
    # Create the complementary color
    comp_h = (h + 0.5) % 1.0
    
    # Generate variations around both the base and complementary colors
    palette = []
    for i in range(num_colors):
        if i < num_colors // 2:
            # Base color variations
            new_h = (h + (i * 0.02)) % 1.0
            new_s = max(0.2, min(1.0, s * (0.7 + i/(num_colors*2))))
            new_v = max(0.3, min(1.0, v * (0.8 + i/(num_colors*2))))
        else:
            # Complementary color variations
            new_h = (comp_h + ((i - num_colors // 2) * 0.02)) % 1.0
            new_s = max(0.2, min(1.0, s * (0.7 + (i - num_colors // 2)/(num_colors*2))))
            new_v = max(0.3, min(1.0, v * (0.8 + (i - num_colors // 2)/(num_colors*2))))
        
        # Convert to RGB
        rgb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
        rgb_255 = tuple(int(c * 255) for c in rgb)
        
        palette.append(Color(rgb_255))
    
    return palette


def _generate_triadic(base_color, num_colors):
    """Generate a triadic palette (three colors equally spaced on the color wheel)."""
    h, s, v = base_color.hsv
    
    # Create the triadic colors
    h1 = h
    h2 = (h + 1/3) % 1.0
    h3 = (h + 2/3) % 1.0
    
    palette = []
    for i in range(num_colors):
        # Distribute colors among the three hues
        if i % 3 == 0:
            new_h = h1
        elif i % 3 == 1:
            new_h = h2
        else:
            new_h = h3
        
        # Vary saturation and value slightly
        idx = i // 3
        new_s = max(0.3, min(1.0, s * (0.8 + idx * 0.1)))
        new_v = max(0.4, min(1.0, v * (0.9 + idx * 0.05)))
        
        # Convert to RGB
        rgb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
        rgb_255 = tuple(int(c * 255) for c in rgb)
        
        palette.append(Color(rgb_255))
    
    return palette


def _generate_tetradic(base_color, num_colors):
    """Generate a tetradic palette (four colors forming a rectangle on the color wheel)."""
    h, s, v = base_color.hsv
    
    # Create the tetradic colors
    h1 = h
    h2 = (h + 0.25) % 1.0
    h3 = (h + 0.5) % 1.0
    h4 = (h + 0.75) % 1.0
    
    palette = []
    for i in range(num_colors):
        # Distribute colors among the four hues
        if i % 4 == 0:
            new_h = h1
        elif i % 4 == 1:
            new_h = h2
        elif i % 4 == 2:
            new_h = h3
        else:
            new_h = h4
        
        # Vary saturation and value slightly
        idx = i // 4
        new_s = max(0.3, min(1.0, s * (0.8 + idx * 0.1)))
        new_v = max(0.4, min(1.0, v * (0.9 + idx * 0.05)))
        
        # Convert to RGB
        rgb = colorsys.hsv_to_rgb(new_h, new_s, new_v)
        rgb_255 = tuple(int(c * 255) for c in rgb)
        
        palette.append(Color(rgb_255))
    
    return palette
