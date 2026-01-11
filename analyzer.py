import ast

def analyze_code(code):
    tree = ast.parse(code)

    functions = []
    classes = []
    undocumented = []

    for node in ast.walk(tree):

        # ---------- FUNCTION DETECTION ----------
        if isinstance(node, ast.FunctionDef):
            returns = []
            logic_elements = []

            for n in ast.walk(node):
                if isinstance(n, ast.Return) and n.value is not None:
                    returns.append(ast.dump(n.value))

                if isinstance(n, ast.If):
                    logic_elements.append("Conditional branching (if/else)")

                if isinstance(n, (ast.For, ast.While)):
                    logic_elements.append("Loop-based iteration")

            func_info = {
                "type": "function",
                "name": node.name,
                "params": [arg.arg for arg in node.args.args],
                "docstring": ast.get_docstring(node),
                "has_return": len(returns) > 0,
                "logic": logic_elements
            }

            functions.append(func_info)

            if func_info["docstring"] is None:
                undocumented.append(f"Function: {node.name}")

        # ---------- CLASS DETECTION ----------
        elif isinstance(node, ast.ClassDef):
            methods = []

            for body_item in node.body:
                if isinstance(body_item, ast.FunctionDef):
                    methods.append(body_item.name)

            class_info = {
                "type": "class",
                "name": node.name,
                "methods": methods,
                "docstring": ast.get_docstring(node)
            }

            classes.append(class_info)

            if class_info["docstring"] is None:
                undocumented.append(f"Class: {node.name}")

    return functions, classes, undocumented



