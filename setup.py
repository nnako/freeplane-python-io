from setuptools import setup, find_packages

# get long description that is used within the README file of this project
# (available on the GitHub platform) for display within PyPi platform

with open("README.rst", "r") as fh:
    long_description = fh.read()

# for obtaining current version information directly from the source code, the
# local freeplane code file is to be consulted, prior to its installation on
# the local system. as it seems that at this point of the operation no LXML
# package is available (although it had previously been installed), its import
# statement within freeplane.py must be held in try / except clause.

import src.freeplane as freeplane

# do the settings for PyPi
setup(
    name='freeplane-io',
    #version="0.7.2",
    version=freeplane.__version__,
    py_modules=['freeplane'],
    author='nnako',
    author_email='nnako@web.de',
    url="https://github.com/nnako/freeplane-python-io",
    description='provide create, read, update and delete of freeplane nodes via file access',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        # "html2text ~= 2020.1.16",
        "lxml",
        "pytest >= 8.0.0",
        "pytest-cov",
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        ],
    extras_require={
        "doc": [
            "sphinx~=5.2.3",
            ],
        },
)
