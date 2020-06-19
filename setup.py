from setuptools import setup, find_packages


setup(
    name='bestpix',
    version='1.3.6',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    scripts=['scripts/reveal', 'scripts/cleanup'],
    license='GNU GPLv3',
    author='Michael Chuprin',
    author_email='mkchuprin@gmail.com',
    url='https://github.com/mkchuprin/BestPix',
    packages=['bestpix'],
    include_package_data=True,
)