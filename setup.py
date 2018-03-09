#!/usr/bin/env python3
import os
import glob
import setuptools


# loads __version__ from version submodule
package_name = 'abm'
path = \
    os.path.join(os.path.dirname(__file__), 'src', package_name, 'version.py')
with open(path, 'r') as f:
    exec(f.read())


setuptools.setup(
    name=package_name,
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
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[os.path.splitext(os.path.basename(path))[0]
                for path in glob.glob('src/*.py')]
)
