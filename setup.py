from setuptools import setup, find_packages

setup(
    name='my_postcode_lib',
    version='0.1',
    author='Sam Meehan',
    author_email='sammeehansam@gmail.com',
    packages=find_packages(),
    description='A simple library for validating and formatting UK postcodes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
