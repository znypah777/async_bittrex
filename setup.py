from setuptools import setup

setup(name='pyasync-bittrex',
      version='0.0.1',
      url = "https://github.com/halcyonjuly7/async_bittrex",
      packages=['async_bittrex'],
      modules=['async_bittrex'],
      install_requires=["aiohttp>=2.3.5",
                        "async - timeout>=2.0.0",
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