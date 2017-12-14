import os
from setuptools import setup, find_packages



setup(name='async_bittrex',
      version='0.0.1',
      url = "https://github.com/halcyonjuly7/async_bittrex",
      packages=find_packages(exclude=[".docs/", ".venv/"]),
      install_requires=["aiohttp>=2.3.5",
                        "async-timeout>=2.0.0",
                        "chardet>=3.0.4",
                        "multidict>=3.3.2",
                        "yarl>=0.15.0"
                        ],
      description='async Python bindings for bittrex API.',
      author='Halcyon Ramirez',
      author_email='znypah777@gmail.com',
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Operating System :: OS Independent',
          'Topic :: Office/Business :: Financial',
      ])