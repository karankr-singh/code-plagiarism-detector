import ast

def parse_code_to_ast(code: str):
    """
    Converts source code into an AST.
    Returns None if syntax is invalid.
    """
    try:
        return ast.parse(code)
    except SyntaxError:
        return None


class ASTNormalizer(ast.NodeTransformer):
    """
    Removes superficial differences like:
    - variable names
    - function names
    - argument names
    - literal values
    """

    # Replace variable names
    def visit_Name(self, node):
        return ast.copy_location(
            ast.Name(id="VAR", ctx=node.ctx),
            node
        )

    # Replace function arguments
    def visit_arg(self, node):
        return ast.copy_location(
            ast.arg(arg="VAR", annotation=None),
            node
        )

    # Replace function names
    def visit_FunctionDef(self, node):
        node.name = "FUNC"
        self.generic_visit(node)
        return node

    # Replace constant values (numbers, strings)
    def visit_Constant(self, node):
        return ast.copy_location(
            ast.Constant(value="CONST"),
            node
        )


def normalize_ast(tree: ast.AST):
    """
    Applies normalization to AST
    """
    normalizer = ASTNormalizer()
    normalized_tree = normalizer.visit(tree)
    ast.fix_missing_locations(normalized_tree)
    return normalized_tree

def ast_to_sequence(tree: ast.AST):
    """
    Converts AST into a sequence of node types.
    This makes comparison easy and robust.
    """
    sequence = []

    for node in ast.walk(tree):
        sequence.append(type(node).__name__)

    return sequence
