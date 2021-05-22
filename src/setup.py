import os
from setuptools import setup

setup(
    name = "pelican",
    version = "0.1",
    author = "Sean Mattingly",
    author_email = "Smattacus@gmail.com",
    description = ("Simple github runner stuff."),
    license = "none",
    keywords = "example documentation tutorial",
    url = "",
    packages=['pelican'],
    long_description='',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        "click",
    ]
)