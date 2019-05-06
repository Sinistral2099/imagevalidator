from setuptools import setup, find_packages

import os
import re
import sys

VERSION = "0.1.0"

PY3 = sys.version_info[0] == 3
HERE = os.path.dirname(os.path.abspath(__file__))


def get_version():
    filename = os.path.join(HERE, 'validators', '__init__.py')
    with open(filename) as f:
        contents = f.read()
    pattern = r"^__version__ = '(.*?)'$"
    return re.search(pattern, contents, re.MULTILINE).group(1)


extras_require = {
    "test": [
        "pytest>=2.2.3",
        "flake8>=2.4.0",
        "isort>=4.2.2",
        "pillow>=3.4.2"
    ],
}

install_requires = [
    "validators>=0.12.5"
]


setup(
    name="imagevalidator",
    version=get_version,
    packages=find_packages('.', exclude=['tests', 'tests.*']),
    description="A python library for easy validation of images.",
    author="David Rose",
    author_email="shirizaan@gmail.com",
    license="MIT",
    url="https://github.com/shirizaan/imagevalidator",
    download_url="https://github.com/shirizaan/imagevalidator/tarball/{}".format(VERSION),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    build_requires=install_requires,
    extras_require=extras_require,
    entry_points={},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
