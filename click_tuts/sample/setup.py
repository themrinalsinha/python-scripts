from setuptools import  setup

setup(
    name='samplecli',
    version='0.0.1',
    py_modules=['app'],
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        yoyo=app:cli
    ''',
)
