"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the ad_works project.
"""
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

import ad_works

setup(
    name="ad_works",
    version=ad_works.__version__,
    url="https://databricks.com",
    author="shaun.ryan@shaunchiburihotmail.onmicrosoft.com",
    description="wheel file based on ad_works/src",
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    entry_points={
        "packages": [
            "main=ad_works.main:main"
        ]
    },
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools"
    ],
)
