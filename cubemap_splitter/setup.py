import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cubemap_splitter",
    version="0.1.7",
    description="Python library for automatically splitting and writing cubemap subset images",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/paulburgess1357/Cubemap-Splitter",
    author="Paul Burgess",
    author_email="paulburgess1357@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["cubemap_splitter"],
    include_package_data=True,
    install_requires=["opencv-python", "numpy<=1.19.3"],
)
