#!/usr/bin/env python3
from glob import glob
from setuptools import setup, find_packages


PACKAGE_NAME = 'abm'


# loads __version__ from version submodule
path = os.path.join(os.path.dirname(__file__),
                    PACKAGE_NAME,
                    'version.py')
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
    install_requires=[
        'requests',
        'pyyaml'
    ],
    include_package_data=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
#    entry_points = {
#        'console_scripts': [ 'abm = abm.cli:main' ]
#    },
#    test_suite = 'tests'
)
