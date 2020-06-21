from setuptools import setup, find_packages


setup(
    name='bestpix',
    version='1.4.9',
    author='Michael Chuprin',
    author_email='mkchuprin@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mkchuprin/BestPix',
    scripts=['scripts/reveal', 'scripts/cleanup'],
    license='GNU GPLv3',
    packages=['bestpix'],
    include_package_data=True,
    python_requires='>=3',
)