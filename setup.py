from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="menu",
    version="1.0.0",
    author="Erik"
    author_email="", # Empty for now as the setup.py is not supposed to be used yet.
    description="A commandline menu program written for users that love commandline in Python using curses.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erikkamph/menu",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.7'
)
