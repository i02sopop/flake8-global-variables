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

from collections import namedtuple


class Visitor(ast.NodeVisitor):
    defined_error = 'Global variable {0} defined'
    used_error = 'Global variable {0} used'
    Error = namedtuple('Error', ['lineno', 'code', 'message'])

    def __init__(self):
        self.errors = []

    def visit_Assign(self, node):
        if node.col_offset == 0:
            for target in node.targets:
                if not hasattr(target, 'id'):
                    continue

                # We consider that the variables in upper case are constants,
                # not global variables.
                if not target.id.isupper():
                    err = self.Error(node.lineno, 'W001',
                                     self.defined_error.format(target.id))
                    self.errors.append(err)

        super(Visitor, self).generic_visit(node)

    def visit_Global(self, node):
        for name in node.names:
            # We consider that the variables in upper case are constants,
            # not global variables.
            if not name.isupper():
                err = self.Error(node.lineno, 'W002',
                                 self.used_error.format(name))
                self.errors.append(err)
        super(Visitor, self).generic_visit(node)
