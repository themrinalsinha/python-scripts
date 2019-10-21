# ====================================
# ==== Other Pretty Cool Features ====
# ====================================

# So far, you’ve seen the headline news regarding what’s new in Python 3.8.
# However, there are many other changes that are also pretty cool.
# In this section, you’ll get a quick look at some of them.

# importlib.metadata
# There is no new module available in the standard library in Python 3.8
# using importlib.metadata you can access information about installed packages
# in your python installation. Together with its companion module, importlib.resources
# importlib.metadata improves on the functionality f the pkg_resources.

from importlib import metadata
print(metadata.version('pip'))

pip_metadata = metadata.metadata('pip')    # gives pip version
print(list(pip_metadata))
print(pip_metadata['Home-page'])
print(pip_metadata['Requires-Python'])
print(metadata.files('pip'))               # with files(), you get a listing of all
                                           # files that make up the pip packages.

# files() returns list of Path objects. These give you a convenient way of looking into
# the source code of a package, using read_text().

# To access package depencencies:
print(metadata.requires('pip'))

# requires() lists the dependencies of a package. There is a backport of importlib.metadata
# available on PyPI that works on earlier versions of python. You can install it using pip.
# $ python -m pip install importlib-metadata

# You can fall back on using the PyPI backport in your code as follows:
# try:
#     from importlib import metadata
# except ImportError:
#     import importlib_metadata as metadata

# ....
