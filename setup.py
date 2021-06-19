from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='json_server',
    version='0.1.3',
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'click',
        'flask',
        'flask-cors'
    ],
    entry_points={
        'console_scripts': [
            'json_server = json_server:cli_command',
        ],
    },
    url="https://github.com/YuvrajGeek/json-server"
)
