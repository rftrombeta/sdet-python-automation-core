import re
from setuptools import setup, find_packages

PACKAGE_NAME = 'sdet_python_automation_core'
SOURCE_DIRECTORY = 'src'
SOURCE_PACKAGE_REGEX = re.compile(rf'^{SOURCE_DIRECTORY}')

source_packages = find_packages(include=[SOURCE_DIRECTORY, f'{SOURCE_DIRECTORY}.*'])
proj_packages = [SOURCE_PACKAGE_REGEX.sub(PACKAGE_NAME, name) for name in source_packages]

setup(
    name=PACKAGE_NAME,
    packages=proj_packages,
    package_dir={PACKAGE_NAME: SOURCE_DIRECTORY},
    description='Funções úteis e aplicáveis em todos os projetos de automação com Python e Robot Framework',
    url='https://github.com/rftrombeta/sdet-python-automation-core',
    author='Rodrigo Trombeta',
    author_email='rftrombeta@gmail.com',
    python_requires='>=3.11.0',
    install_requires=['certifi',
                      'collection',
                      'curlify',
                      'dateutils',
                      'faker',
                      'mimesis',
                      'pytz',
                      'python-dotenv',
                      'robotframework',
                      'robotframework-faker',
                      'robotframework-jsonlibrary',
                      'robotframework-metrics',
                      'robotframework-pabot',
                      'robotframework-requests',
                      'requests',
                      'xmltodict']
)