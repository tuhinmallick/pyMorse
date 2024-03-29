import pathlib

from setuptools import find_packages
from setuptools import setup

HERE = pathlib.Path(__file__).parent

VERSION = "0.0.1"
PACKAGE_NAME = "pyMorse"
AUTHOR = "Tuhin Mallick"
AUTHOR_EMAIL = "tuhin.mllk@gmail.com"
URL = "https://github.com/tuhinmallick/pyMorse"
KEYWORDS = "rsa email-sender python cryptography smtp"

LICENSE = "MIT License"
DESCRIPTION = "Conceal your emails with Python"
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = ["numpy", "smtplib", "email"]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    keywords=KEYWORDS,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
)
