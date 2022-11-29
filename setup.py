from os import path
from setuptools import setup

# Read the contents of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def version_scheme(version):
    """
    Version scheme hack for setuptools_scm.

    Appears to be necessary to due to the bug documented here: https://github.com/pypa/setuptools_scm/issues/342

    If that issue is resolved, this method can be removed.
    """
    import time

    from setuptools_scm.version import guess_next_version

    if version.exact:
        return version.format_with("{tag}")
    else:
        _super_value = version.format_next_version(guess_next_version)
        now = int(time.time())
        return _super_value + str(now)


def local_version(version):
    """
    Local version scheme hack for setuptools_scm.

    Appears to be necessary to due to the bug documented here: https://github.com/pypa/setuptools_scm/issues/342

    If that issue is resolved, this method can be removed.
    """
    return ""


setup(
    name='census-data-downloader',
    description="Download U.S. census data and reformat it for humans",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Los Angeles Times Data and Graphics Department',
    author_email='datadesk@latimes.com',
    url='http://www.github.com/datadesk/census-data-downloader',
    license="MIT",
    packages=(
        "census_data_downloader",
        "census_data_downloader.core",
        "census_data_downloader.tables",
    ),
    install_requires=(
        "pandas",
        "us",
        "census",
        "census-data-aggregator",
        "click",
        "jinja2"
    ),
    entry_points="""
        [console_scripts]
        censusdatadownloader=census_data_downloader.cli:cmd
    """,
    setup_requires=["setuptools_scm",],
    use_scm_version={"version_scheme": version_scheme, "local_scheme": local_version},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
)
