from distutils.core import setup, find_packages
from __init__ import VERSION

setup(name='Snowflake',
      version=VERSION,
      description='Snowflake generator.',
      author='JohnyTheCarrot',
      author_email='johnythecarrot@gmail.com',
      url='https://github.com/JohnyTheCarrot/snowflake',
      packages=find_packages()
)
