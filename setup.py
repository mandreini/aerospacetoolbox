from setuptools import setup, find_packages

setup(
    name = 'aerospacetoolbox',
    version = '0.93',
    description = 'Aerospace Toolbox',
    author = 'Wilco Schoneveld, python 3.x port by Matthew Andreini',
    author_email = 'schoneveld.wj@gmail.com / matthew@andreini.us',
    url = 'https://github.com/wilcoschoneveld/aerospacetoolbox / https://github.com/mandreini/aerospacetoolbox',
    install_requires = ['scipy'],
    packages = find_packages(exclude=['tests']),
    package_data = {
        '': ['egm96.dac']
    }
)
