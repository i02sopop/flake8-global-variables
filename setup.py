import os
import setuptools

base_dir = os.path.dirname(__file__)
about = {}
with open(os.path.join(base_dir, "flake8_global_variables", "__init__.py")) as f:
    exec(f.read(), about)

setuptools.setup(
    name=about["__title__"],
    license="MIT",
    version=about["__version__"],
    description=about["__summary__"],
    author=about["__author__"],
    author_email=about["__email__"],
    maintainer=about['__maintainer__'],
    maintainer_email=about['__maintainer_email__'],
    url="https://github.com/i02sopop/flake8-global-variables",

    packages=[
        "flake8_global_variables",
    ],

    install_requires=[
        "flake8 > 3.0.0",
    ],

    entry_points={
        'flake8.extension': [
            'W = flake8_global_variables.globalvariables:GlobalVariables',
        ],
    },

    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
