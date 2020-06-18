from setuptools import setup, find_packages


setup(
    name='bestpix',
    version='1.2',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    scripts=['scripts/reveal'],
    license='GNU GPLv3',
    author='Michael Chuprin',
    author_email='mkchuprin@gmail.com',
    url='https://github.com/mkchuprin/BestPix',
    install_requires=['Flask==1.1.2', 'pyheif==0.4', 'Pillow==7.1.2'],
    packages=['bestpix']
)