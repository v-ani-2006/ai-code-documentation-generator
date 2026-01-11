def generate_readme(functions, classes):
    function_names = [f["name"] for f in functions]
    class_names = [c["name"] for c in classes]

    readme = f"""
# AI Code Documentation Generator

## 📌 Overview
This project automatically analyzes Python source code and generates
clear documentation for functions and classes.

## 🚀 Features
- Function documentation
- Parameter explanations
- Return value detection
- Class and method summaries
- Automatic README generation

## 📂 Detected Components

### Classes
{', '.join(class_names) if class_names else 'No classes detected'}

### Functions
{', '.join(function_names) if function_names else 'No functions detected'}

---
Generated using AI Code Documentation Generator
"""
    return readme.strip()


def generate_documentation(functions, classes):
    docs = []

    # Add README first
    docs.append(generate_readme(functions, classes))

    # ---------- CLASS DOCUMENTATION ----------
    for cls in classes:
        methods = "\n".join(cls["methods"]) if cls["methods"] else "No methods defined"

        class_doc = f"""
Class Name:
{cls['name']}

Description:
This class groups related functionality.

Methods:
{methods}
"""
        docs.append(class_doc.strip())

    # ---------- FUNCTION DOCUMENTATION ----------
    for func in functions:
        params = "\n".join(
            f"{p} : parameter of {func['name']}()" for p in func["params"]
        ) if func["params"] else "None"

        return_text = (
            "Returns a value" if func["has_return"]
            else "Does not return any value"
        )

        logic = "\n".join(f"- {l}" for l in func["logic"]) if func["logic"] else "No complex logic detected"

        func_doc = f"""
Function Name:
{func['name']}

Parameters:
{params}

Description:
This function performs operations defined in the source code.

Logic Explanation:
{logic}

Returns:
{return_text}
"""
        docs.append(func_doc.strip())

    return docs




