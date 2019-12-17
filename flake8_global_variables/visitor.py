import ast

from collections import namedtuple

Error = namedtuple('Error', ['lineno', 'code', 'message'])


class Visitor(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
        self.errors = []

    def visit_Assign(self, node):
        if node.col_offset == 0:
            for target in node.targets:
                # print(self.filename, ': Global variable', target.id, 'defined in line', node.lineno)
                self.errors.append(Error(node.lineno, 'W001',
                                         'Global variable {0} defined'.format(target.id)))

        super(Visitor, self).generic_visit(node)

    def visit_Global(self, node):
        for name in node.names:
            self.errors.append(Error(node.lineno, 'W002',
                                     'Global variable {0} used'.format(name)))
        super(Visitor, self).generic_visit(node)
