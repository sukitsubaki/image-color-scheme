from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="image-color-scheme",
    version="0.2.1",
    author="Suki Tsubaki",
    author_email="",
    description="Extract dominant colors from images and create color palettes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sukitsubaki/image-color-scheme",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Artistic Software",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pillow>=8.0.0",
        "numpy>=1.19.0",
    ],
)
