# setup.py
# Configuração para distribuição do pacote
import os

from setuptools import setup, find_packages

# Carregar o conteúdo de requirements.txt
with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="CSVJoiner",
    version="0.1",
    packages=find_packages(where='src', exclude=[]),
    package_dir={'': 'src'},
    install_requires=required,
    entry_points={
        "console_scripts": [
            "csv-joiner=main:main",
        ],
    },
)