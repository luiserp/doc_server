from pathlib import Path
import setuptools

if __name__ == '__main__':

    # read the contents of your README file
    this_directory = Path(__file__).parent
    long_description = (this_directory / "README.md").read_text()

    setuptools.setup (
        name='doc_server',
        version='0.1',
        # This automatically detects the packages in the specified
        # (or current directory if no directory is given).
        packages=setuptools.find_packages(),
        # The entry points are the big difference between
        # setuptools and distutils, the entry points make it
        # possible to extend setuptools and make it smarter and/or
        # add custom commands.
        entry_points={
            # The following would make these functions callable as
            # standalone scripts. In this case it would add the
            # spam command to run in your shell.
            'console_scripts': [
                'doc_server = doc_server.__main__:main',
            ],
        },
        # Packages required to use this one, it is possible to
        # specify simply the application name, a specific version
        # or a version range. The syntax is the same as pip
        # accepts.
        install_requires=[],
        # Extra requirements are another amazing feature of
        # setuptools, it allows people to install extra
        # dependencies if you are interested. In this example
        # doing a "pip install name[all]" would install the
        # python-utils package as well.
        extras_requires={
            'all': [],
        },
        # Packages required to install this package, not just for
        # running it but for the actual install. These will not be
        # installed but only downloaded so they can be used during
        # the install. The pytest-runner is a useful example:
        setup_requires=[],
        # The requirements for the test command. Regular testing
        # is possible through: python setup.py test The Pytest
        # module installs a different command though: python
        # setup.py pytest
        tests_require=[],
        # The package_data, include_package_data and
        # exclude_package_data arguments are used to specify which
        # non-python files should be included in the package. An
        # example would be documentation files. More about this
        # in the next paragraph
        package_data={
            # Include (restructured text) documentation files from
            # any directory
            '': ['*.rst'],
            # Include text files from the eggs package:
            'eggs': ['*.txt'],
        },
        # If a package is zip_safe the package will be installed
        # as a zip file. This can be faster but it generally
        # doesn't make too much of a difference and breaks
        # packages if they need access to either the source or the
        # data files. When this flag is omitted setuptools will
        # try to autodetect based on the existance of datafiles
        # and C extensions. If either exists it will not install
        # the package as a zip. Generally omitting this parameter
        # is the best option but if you have strange problems with
        # missing files, try disabling zip_safe.
        zip_safe=False,
        # All of the following fileds are PyPI metadata fields.
        # When registering a package at PyPI this is used as
        # information on the package page.
        author='Luis Enrique Reyes P??rez',
        author_email='luisreyesperez98@gmail.com',
        # This should be a short description (one line) for the
        # package
        description='Manage and review documentations of some languages and technologies',
        # For this parameter I would recommend including the
        # README.rst
        long_description=long_description,
        long_description_content_type='text/markdown',
        # The license should be one of the standard open source
        # licenses: https://opensource.org/licenses/alphabetical
        license='MIT',
        url='https://github.com/luiserp/doc_server'
    )