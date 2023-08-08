import os, glob

from setuptools import setup, find_packages

HERE = os.path.dirname(os.path.abspath(__file__))


# with open('requirements.txt') as f:
#     requirements = f.read().splitlines()
#     requirements = [r for r in requirements if not r.startswith('-e')]


# packages = ['djow'] + glob.glob('djow_*')

setup(
    name='HarmonicPatterns',
    version='0.0.2',
    # install_requires=requirements,
    packages=find_packages(where='src',
                           exclude=["res",
                                    "examples",]),
    package_dir={'HarmonicPatterns': 'src'},
    python_requires='>=3.8',
    url='https://github.com/xeonvs/HarmonicPatterns',
    author='djoffrey',
    author_email='joffrey.oh@gmail.com',
    description='A Python Library for Harmonic Trading'
)
