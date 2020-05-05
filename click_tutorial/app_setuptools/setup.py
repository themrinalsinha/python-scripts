from setuptools import setup

setup(
    name='timepass',
    version="0.0.1",
    py_modules=['app_setuptools'] # or find_packages()
    install_requires=['click']

    # we'll have to create entrypoint
    entry_points="""
        [console_script]
        timepass=app_setuptools:main
    """
)
