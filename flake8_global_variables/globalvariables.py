import ast

from visitor import Visitor

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

    def chech_words(self):
        if not self.tree or not self.lines:
            self.load_file()

        visitor = Visitor()
        visitor.visit(self.tree)

def register_opt(parser, *args, **kwargs):
    parser.add_option(*args, **kwargs)
