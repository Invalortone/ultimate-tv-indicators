from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Famous Tradingview Indicators in Python'

# Setting up
setup(
    name="ultimate-tv-indicators",
    version=VERSION,
    author="Invalortone",
    author_email="<invelortone1610@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['math', 'pandas'],
    keywords=['python', 'tradingview', 'indicators', 'pinescript', 'finance', 'freqtrade'],
    classifiers=[
        "Development Status :: Alpha",
        "Intended Audience :: Traders",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
