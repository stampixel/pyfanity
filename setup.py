from setuptools import setup, find_packages

VERSION = "0.1.0"
DESCRIPTION = "A simple and light weight profanity filter package."
LONG_DESCRIPTION = ""

REQUIREMENTS = [
    ""
]

setup(
    name="pyfanity",
    version="0.0.1",
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
