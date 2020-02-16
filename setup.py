from setuptools import find_packages
from distutils.core import setup

setup(
    name='xkci-cli',
    version='0.0.1',
    packages=find_packages(),
    license='MIT',
    include_package_data=True,
    author='Nikhil Deepak Shinde',
    author_email='crenickshinde1996@gmail.com',
    download_url='',
    install_requires=[
        'Click',
    ],
    keywords = ['web-comic', 'xkcd', 'cli'],
    entry_points='''
        [console_scripts]
        xkcd=src.cli:cli
    ''',
)