"""
File not currently in use, please view pyproject.toml instead
"""

from setuptools import setup, find_packages

VERSION = "0.1.1"
DESCRIPTION = "A simple and lightweight profanity filter package."
LONG_DESCRIPTION = ""

REQUIREMENTS = [
    ""
]

setup(
    name="pyfanity",
    version=VERSION,
    author="Kevin Tang",
    author_email="stampixel@pm.me",
    license="MIT",
    url="https://github.com/stampixel/pyfanity",
    install_requires=REQUIREMENTS,
    keywords=[
        "profanity",
        "profanity blocker",
        "swear",
        "langauge",
        "language-filter",
    ],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
