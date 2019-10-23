"""Setup."""
import path
from setuptools import setup, find_packages


base_dir = path.abspath(path.dirname(__file__))

with open(path.join(base_dir, 'README.md')) as desc:
    long_description = desc.read()

with open(path.join(base_dir, 'LICENSE')) as desc:
    license = desc.read()

with open(path.join(base_dir, 'version.py')) as version:
    exec(version.read())

setup(
    name='angelos_lab',
    version=__version__,  # noqa F821
    description='A laboratory environment for the Angelos project.',
    long_description=long_description,
    author=__author__,  # noqa F821
    author_email=__author_email__,  # noqa F821
    url=__url__,  # noqa F821
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
