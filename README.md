# image-color-scheme

Extract dominant colors from images and create beautiful color palettes with minimal dependencies.

![Version](https://img.shields.io/badge/version-0.2.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- Extract dominant colors from any image format supported by Pillow
- Generate harmonious color palettes
- Customize number of colors to extract
- Export palettes in various formats (RGB, HEX, HSV)
- Minimal dependencies (only requires Pillow and NumPy)

## Installation

```bash
pip install image-color-scheme
```

Or install from source:

```bash
git clone https://github.com/sukitsubaki/image-color-scheme.git
cd image-color-scheme
pip install -e .
```

## Quick Start

```python
from image_color_scheme import extract_colors, generate_palette

# Extract 5 dominant colors from an image
colors = extract_colors("path/to/image.jpg", num_colors=5)

# Generate a palette from the colors
palette = generate_palette(colors)

# Print the colors in HEX format
for color in palette:
    print(color.hex)
```

## Example

```python
from image_color_scheme import extract_colors
import matplotlib.pyplot as plt
import numpy as np

# Extract colors from image
colors = extract_colors("landscape.jpg", num_colors=6)

# Display the colors as a palette
plt.figure(figsize=(10, 2))
for i, color in enumerate(colors):
    plt.fill_between([i, i+1], 0, 1, color=color.rgb_normalized)
    
plt.xticks([])
plt.yticks([])
plt.show()
```

## Documentation

For more detailed usage examples and documentation, see the [usage guide](docs/usage.md).

## Requirements

- Python 3.7+
- Pillow
- NumPy

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.