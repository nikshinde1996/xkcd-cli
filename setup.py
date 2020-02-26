from setuptools import find_packages
from distutils.core import setup

setup(
    name='xkcd-cli',
    version='0.0.2',
    packages=find_packages(),
    license='MIT',
    include_package_data=True,
    author='Nikhil Deepak Shinde',
    author_email='crenickshinde1996@gmail.com',
    download_url='',
    install_requires=[
        'Click',
        'requests',
        'pillow'
    ],
    keywords = ['web-comic', 'xkcd', 'cli'],
    entry_points='''
        [console_scripts]
        xkcd=src.cli:cli
    ''',
)