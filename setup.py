from setuptools import setup, find_packages

setup(
    name='imessage_reader',
    version='1.0.1',
    license='MIT',
    description='Fetch recipients and chat messages from the chat.db database.',

    author='Bodo Schönfeld',
    author_email='bodo.schoenfeld@niftycode.de',
    url='https://github.com/niftycode/imessage_reader',

    packages=find_packages(exclude=('tests', 'docs')),

    install_requires=['pytest'],
    tests_require=['pytest'],
)
