# Usage Guide

`image-color-scheme` provides a simple interface for extracting dominant colors from images and generating harmonious color palettes.

## Installation

First, install the package using pip:

```bash
pip install image-color-scheme
```

## Basic Usage

### Extracting Colors

To extract the dominant colors from an image:

```python
from image_color_scheme import extract_colors

# Extract 5 dominant colors (default)
colors = extract_colors("path/to/image.jpg")

# Extract a specific number of colors
colors = extract_colors("path/to/image.jpg", num_colors=8)

# Display color information
for color in colors:
    print(f"RGB: {color.rgb}, HEX: {color.hex}")
```

### Generating Palettes

Once you have extracted colors, you can generate different types of color palettes:

```python
from image_color_scheme import generate_palette, PaletteType

# Extract colors from an image
colors = extract_colors("path/to/image.jpg")

# Generate a monochromatic palette (default)
mono_palette = generate_palette(colors)

# Generate an analogous palette with 6 colors
analogous_palette = generate_palette(
    colors, 
    palette_type=PaletteType.ANALOGOUS,
    num_colors=6
)

# Generate a complementary palette
complementary_palette = generate_palette(
    colors, 
    palette_type=PaletteType.COMPLEMENTARY
)

# Generate a triadic palette
triadic_palette = generate_palette(
    colors, 
    palette_type=PaletteType.TRIADIC
)

# Generate a tetradic palette
tetradic_palette = generate_palette(
    colors, 
    palette_type=PaletteType.TETRADIC
)
```

## Color Object Methods

The `Color` class provides several useful properties:

```python
# Get a color from the extracted colors
color = colors[0]

# RGB values (0-255)
print(color.rgb)  # e.g., (255, 128, 64)

# Normalized RGB values (0-1)
print(color.rgb_normalized)  # e.g., (1.0, 0.5, 0.25)

# HEX code
print(color.hex)  # e.g., "#ff8040"

# HSV values
print(color.hsv)  # e.g., (0.083, 0.749, 1.0)
```

## Visualization

To visualize the extracted colors or generated palettes, you can use the included example script or write your own visualization code:

```python
import matplotlib.pyplot as plt
from image_color_scheme import extract_colors, generate_palette, PaletteType

# Extract colors
colors = extract_colors("path/to/image.jpg", num_colors=5)

# Generate a palette
palette = generate_palette(colors, palette_type=PaletteType.ANALOGOUS)

# Create a figure
plt.figure(figsize=(10, 2))

# Plot each color as a rectangle
for i, color in enumerate(palette):
    plt.fill_between([i, i+1], 0, 1, color=color.rgb_normalized)

# Remove axes ticks
plt.xticks([])
plt.yticks([])
plt.title("Color Palette")
plt.show()
```

## Advanced Usage

### Resizing Images

For large images, you might want to resize them before processing to improve performance:

```python
# Extract colors with custom resize settings
colors = extract_colors(
    "path/to/large_image.jpg",
    resize=True,  # Default is True
    max_size=400  # Default is 200
)
```

### Working with PIL Images

If you already have a PIL Image object, you can save it to a temporary file and then process it:

```python
import tempfile
from PIL import Image
from image_color_scheme import extract_colors

# Open an image with PIL
img = Image.open("path/to/image.jpg")

# Process the image (e.g., apply filters)
processed_img = img.filter(ImageFilter.BLUR)

# Save to a temporary file
with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp:
    temp_filename = temp.name
    processed_img.save(temp_filename)

# Extract colors from the processed image
colors = extract_colors(temp_filename)
```

## Command Line Usage

The provided example script can be used as a simple command-line tool:

```bash
# Run the example script
python examples/extract_colors.py path/to/image.jpg
```

This will display the extracted colors and generate various palette types.
