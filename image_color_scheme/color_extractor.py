"""
Color extraction module for image-color-scheme.
"""

import numpy as np
from PIL import Image
from collections import namedtuple
import colorsys


class Color:
    """
    A color class that provides different representations and utilities.
    """
    
    def __init__(self, rgb):
        """
        Initialize a Color with RGB values.
        
        Args:
            rgb (tuple): A tuple of (R, G, B) values between 0 and 255.
        """
        self.rgb = tuple(map(int, rgb))
        
    @property
    def rgb_normalized(self):
        """
        Returns RGB values normalized between 0 and 1.
        """
        return tuple(c/255 for c in self.rgb)
    
    @property
    def hex(self):
        """
        Returns the hex code representation.
        """
        return f"#{self.rgb[0]:02x}{self.rgb[1]:02x}{self.rgb[2]:02x}"
    
    @property
    def hsv(self):
        """
        Returns the HSV representation.
        """
        return colorsys.rgb_to_hsv(*self.rgb_normalized)
    
    def __repr__(self):
        return f"Color(rgb={self.rgb}, hex={self.hex})"


def extract_colors(image_path, num_colors=5, resize=True, max_size=200):
    """
    Extract the dominant colors from an image.
    
    Args:
        image_path (str): Path to the image file.
        num_colors (int): Number of colors to extract.
        resize (bool): Whether to resize the image before processing.
        max_size (int): Maximum size (width or height) if resizing.
        
    Returns:
        list: A list of Color objects representing the dominant colors.
    """
    # Open the image
    img = Image.open(image_path)
    
    # Convert to RGB if not already
    if img.mode != "RGB":
        img = img.convert("RGB")
    
    # Resize image for faster processing if needed
    if resize:
        width, height = img.size
        if width > max_size or height > max_size:
            if width > height:
                new_width = max_size
                new_height = int(height * (max_size / width))
            else:
                new_height = max_size
                new_width = int(width * (max_size / height))
            img = img.resize((new_width, new_height), Image.LANCZOS)
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Reshape the array to be a list of RGB pixels
    pixels = img_array.reshape(-1, 3)
    
    # Use k-means clustering to find the most dominant colors
    from sklearn.cluster import KMeans
    
    # Try to import scikit-learn, but use a simpler method if not available
    try:
        kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init=10)
        kmeans.fit(pixels)
        colors = kmeans.cluster_centers_
    except ImportError:
        # Simple alternative: random sampling and averaging
        print("Warning: scikit-learn not found, using simple sampling method instead.")
        indices = np.random.choice(len(pixels), size=min(1000, len(pixels)), replace=False)
        sampled = pixels[indices]
        
        # Simple clustering
        colors = []
        for _ in range(num_colors):
            if len(sampled) == 0:
                break
            
            # Find the most common color by minimizing distance to all others
            distances = np.sum((sampled[:, np.newaxis, :] - sampled[np.newaxis, :, :]) ** 2, axis=2)
            avg_distances = np.sum(distances, axis=1)
            closest_idx = np.argmin(avg_distances)
            
            # Add the centroid color
            colors.append(sampled[closest_idx])
            
            # Remove similar colors
            mask = np.sum((sampled - sampled[closest_idx]) ** 2, axis=1) > 100
            sampled = sampled[mask]
        
        colors = np.array(colors)
    
    # Convert to Color objects
    return [Color(color) for color in colors]
