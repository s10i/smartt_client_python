import os
import sys

if sys.version_info[:2] < (2, 7) or sys.version_info[0] > 2:
    msg = ("This software was developed for Python 2.7.\n"
           "We have not tested it with any other version.\n" 
           "You are using version %s.\n"
           "Thus, we have not tested with your version. BE CAREFUL!\n" % sys.version)
    sys.stderr.write(msg)

requires = ['setuptools']

from setuptools import setup, find_packages

try:
    here = os.path.abspath(os.path.dirname(__file__))
    README = open(os.path.join(here, 'README.md')).read()
except:
    README = """\
pysmartt - Smartt Python Client """
    CHANGES = ''

CLASSIFIERS = [
    'Environment :: Library',
    'Intended Audience :: Investing strategies programmers',
    'Natural Language :: English',
    'Operating System :: POSIX',
]

dist = setup(
    name = 'pysmartt',
    version = "0.0.1",
    description = "Smartt Python Client",
    classifiers = CLASSIFIERS,
    author = "Felipe Machado",
    author_email = "felipe@s10i.com.br",
    packages = find_packages(),
    install_requires = requires,
    tests_require = requires,
    include_package_data = True,
    zip_safe = False,
    namespace_packages = ['pysmartt'],
    test_suite = "tests",
    entry_points = {
        'console_scripts': [
            'smartt-console = pysmartt.console:main',
        ],
    },
)
