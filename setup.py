from setuptools import setup

VERSION = '0.0.0'

setup(
    name='bud-get',
    version=VERSION,
    description='Budget data utilities.',
    url='http://github.com/doggan/bud-get',
    license='Unlicense',
    author='Shyam Guthikonda',

    packages=['bud_get'],
    entry_points="""
    [console_scripts]
    bud-get = bud_get.cli:main
    """
)
