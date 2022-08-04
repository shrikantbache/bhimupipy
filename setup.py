from codecs import open
from os.path import abspath, dirname, join, expanduser

from setuptools import Command, find_packages, setup

this_dir = abspath(dirname(__file__))

with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='bhimupipy',
    version="0.0.2",
    description="A package to find upi details details",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shrikantbache/bhimupipy.git",
    author="BACHE SHRIKANT GANGADHAR",
    author_email='bacheshrikant@gmail.com',
    maintainer="BACHE SHRIKANT GANGADHAR",
    maintainer_email="bacheshrikant@gmail.com",
    license='MIT',
    license_file="LICENSE",
    platforms="any",

    classifiers=[
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',

    ],
    keywords=['search', 'bhimupijs', 'brute', 'address', 'vpa', 'upi', 'spy'],
    include_package_data=True,
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'bhimupipy=bhimupipy.__init__:ExecuteBhimupiPy',
        ],
    },

)
