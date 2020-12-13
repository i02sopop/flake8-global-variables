# Copyright (C) 2019-2020 Pablo Alvarez de Sotomayor Posadillo

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

import ast
import pycodestyle

from flake8_global_variables import __version__
from flake8_global_variables.visitor import Visitor


class GlobalVariables(object):
    name = "global-variables"
    version = __version__

    def __init__(self, tree, filename, lines=None):
        self.filename = filename
        self.tree = tree
        self.lines = lines

    def error(self, error):
        return (
            error.lineno,
            0,
            "{0} {1}".format(error.code, error.message),
            GlobalVariables,
        )

    def run(self):
        for error in self.check_variables():
            yield error

    def load_file(self):
        if self.filename in ("stdin", "-", None):
            self.filename = "stdin"
            self.lines = pycodestyle.stdin_get_value().splitlines(True)
        else:
            self.lines = pycodestyle.readlines(self.filename)

        if self.tree is None:
            self.tree = ast.parse(''.join(self.lines))

    def check_variables(self):
        if not self.tree or not self.lines:
            self.load_file()

        visitor = Visitor()
        visitor.visit(self.tree)

        for err in visitor.errors:
            yield self.error(err)


def register_opt(parser, *args, **kwargs):
    parser.add_option(*args, **kwargs)
