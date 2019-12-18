# Copyright (C) 2019 Pablo Alvarez de Sotomayor Posadillo

# This file is part of flake8_global_variables.

# flake8_global_variables is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# flake8_global_variables is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#Public License for more details.

# You should have received a copy of the GNU General Public License along with
# flake8_global_variables. If not, see <http://www.gnu.org/licenses/>.

import ast

from collections import namedtuple

Error = namedtuple('Error', ['lineno', 'code', 'message'])


class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.errors = []

    def visit_Assign(self, node):
        if node.col_offset == 0:
            for target in node.targets:
                self.errors.append(Error(node.lineno, 'W001',
                                         'Global variable {0} defined'.format(target.id)))

        super(Visitor, self).generic_visit(node)

    def visit_Global(self, node):
        for name in node.names:
            self.errors.append(Error(node.lineno, 'W002',
                                     'Global variable {0} used'.format(name)))
        uper(Visitor, self).generic_visit(node)
