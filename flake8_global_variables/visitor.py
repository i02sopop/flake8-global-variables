import ast

class Visitor(ast.NodeVisitor):
    def __init__(self, filename):
        self.filename = filename
        self.global_vars = []
        self.lines = []

    def visit_Assign(self, node):
        if node.col_offset == 0:
            for target in node.targets:
                print(self.filename, ': Global variable', target.id, 'defined in line', node.lineno)
            self.lines.append(node.lineno)

    # def visit_Global(self, node):
    #     for name in node.names:
    #         print('Global variable %s in line %d', name.id, node.lineno)
