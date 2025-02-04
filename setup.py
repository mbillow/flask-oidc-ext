import io
import os.path
import sys

from setuptools import setup

# This check is to make sure we checkout docs/_themes before running sdist
if not os.path.exists("./docs/_themes/README"):
    print("Please make sure you have docs/_themes checked out while running setup.py!")
    if os.path.exists(".git"):
        print(
            "You seem to be using a git checkout, please execute the following commands to get the docs/_themes directory:"
        )
        print(" - git submodule init")
        print(" - git submodule update")
    else:
        print(
            "You seem to be using a release. Please use the release tarball from PyPI instead of the archive from GitHub"
        )
    sys.exit(1)


here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, "README.rst")) as f:
    readme = f.read()

setup(
    name="flask-oidc-ext",
    description="OpenID Connect extension for Flask",
    long_description=readme,
    url="https://github.com/svintit/flask-oidc-ext",
    author="Erica Ehrhardt, Patrick Uiterwijk, Traian Svinti",
    author_email="traian.svinti@gmail.com",
    version="1.4.5",
    packages=["flask_oidc_ext"],
    install_requires=[
        "Flask",
        "authlib",
        "oauth2client",
        "six",
    ],
    tests_require=["nose", "mock"],
    entry_points={
        "console_scripts": ["oidc-register=flask_oidc_ext.registration_util:main"],
    },
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
