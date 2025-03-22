#!/usr/bin/env python3
"""
Example script demonstrating how to extract colors from an image
and generate a color palette.

Usage:
    python extract_colors.py path/to/image.jpg
"""

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
from image_color_scheme import extract_colors, generate_palette, PaletteType


def display_colors(colors, title="Extracted Colors"):
    """Display a color palette using matplotlib."""
    # Create a figure with a specific size
    plt.figure(figsize=(10, 2))
    
    # Plot each color as a rectangle
    for i, color in enumerate(colors):
        plt.fill_between([i, i+1], 0, 1, color=color.rgb_normalized)
    
    # Remove axes ticks
    plt.xticks([])
    plt.yticks([])
    
    # Set title
    plt.title(title)
    
    # Show the plot
    plt.show()


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python extract_colors.py path/to/image.jpg")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        sys.exit(1)
    
    try:
        # Extract dominant colors
        print(f"Extracting colors from '{image_path}'...")
        colors = extract_colors(image_path, num_colors=6)
        
        # Display the extracted colors
        print("\nExtracted Colors:")
        for i, color in enumerate(colors):
            print(f"Color {i+1}: RGB {color.rgb}, HEX {color.hex}")
        
        # Display the colors visually
        display_colors(colors)
        
        # Generate different palette types
        palette_types = [
            PaletteType.MONOCHROMATIC,
            PaletteType.ANALOGOUS,
            PaletteType.COMPLEMENTARY,
            PaletteType.TRIADIC,
            PaletteType.TETRADIC
        ]
        
        # Generate and display each palette type
        for palette_type in palette_types:
            palette = generate_palette(colors, palette_type=palette_type, num_colors=5)
            display_colors(palette, title=f"{palette_type.value.capitalize()} Palette")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
