# setup.py
from setuptools import setup, find_packages

setup(
    name="nepali-toolkit",
    version="0.1.0",
    description="A Nepali utility CLI for calendar conversion, NID validation, Unicode ↔ Preeti conversion, and power schedule lookup.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "nepali-datetime",
    ],
    entry_points={
        "console_scripts": [
            "nepcli=nepali_toolkit.cli:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
