from setuptools import setup, find_packages


setup(
    name='BestPix',
    version='1.0',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    scripts=['scripts/reveal'],
    license='GNU GPLv3',
    author='Michael Chuprin',
    author_email='mkchuprin@gmail.com',
    url='https://github.com/mkchuprin/BestPix'
)
