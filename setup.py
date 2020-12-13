# Copyright (C) 2019 Pablo Alvarez de Sotomayor Posadillo

# This file is part of flake8_global_variables.

# flake8_global_variables is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# flake8_global_variables is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.

# You should have received a copy of the GNU General Public License along with
# flake8_global_variables. If not, see <http://www.gnu.org/licenses/>.

import os
import setuptools

base_dir = os.path.dirname(__file__)
about = {}
with open(os.path.join(base_dir, "flake8_global_variables", "__init__.py")) as f:
    exec(f.read(), about)

setuptools.setup(
    name=about["__title__"],
    license="GPLV3",
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
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
