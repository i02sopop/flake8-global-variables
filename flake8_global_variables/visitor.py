import ast

class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.global_vars = []
        self.lines = []

    def visit_Assign(self, node):
        if node.col_offset == 0:
            print('Global variable %s in line %d', name, node.lineno)
            self.lines.append(node.lineno)

    def visit_Global(self, node):
        for name in node.names:
            print('Global variable %s in line %d', name, node.lineno)
