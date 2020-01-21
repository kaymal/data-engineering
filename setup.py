# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='my_package',
      version='0.0.1',
      description='Perform analysis of a given text.',
      author='t k',
      packages=['my_package'],
      install_requires=['matplotlib>=3.0.0'])