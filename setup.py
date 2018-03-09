#!/usr/bin/env python3
import os
from glob import glob
from setuptools import setup, find_packages


# loads __version__ from version submodule
package_name = 'abm'
path = \
    os.path.join(os.path.dirname(__file__), 'src', package_name, 'version.py')
with open(path, 'r') as f:
    exec(f.read())


setup(
    name='abm',
    version=__version__,
    description='TBA',
    long_description='TBA',
    author='TBA',
    author_email='TBA',
    url='https://github.com/squaresLab/AnotherBugMiner',
    license='mit',
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ],
    install_requires=[
        'requests',
        'pyyaml'
    ],
    test_suite='tests',
    include_package_data=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[os.path.splitext(os.path.basename(path))[0]
                for path in glob('src/*.py')]
)
