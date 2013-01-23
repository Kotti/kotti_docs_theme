import os

from setuptools import find_packages
from setuptools import setup

name = 'kotti_docs_theme'
version = '0.1.1'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    README = CHANGES = ''


setup(
    name=name,
    version=version,
    description="Sphinx Theme for Kotti Documentation",
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
    keywords='sphinx theme kotti twitter bootstrap',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/disko/kotti_docs_theme',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Sphinx",
    ],
    entry_points={},
)
