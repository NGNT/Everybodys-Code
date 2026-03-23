import re

LUA_KEYWORDS = {
    "and",
    "break",
    "do",
    "else",
    "elseif",
    "end",
    "false",
    "for",
    "function",
    "if",
    "in",
    "local",
    "nil",
    "not",
    "or",
    "repeat",
    "return",
    "then",
    "true",
    "until",
    "while",
}

COMMON_LUA_FUNCTIONS = {
    "ipairs",
    "pairs",
    "tostring",
    "tonumber",
    "type",
    "math",
    "string",
    "table",
    "print",
}

PLACEHOLDERS = {
    "body_name",
    "shape_name",
    "tag_name",
    "key",
    "myVariable",
    "my_object",
    "sound.ogg",
    "animation_name",
    "bone_name",
    "value",
    "parameter",
    "condition",
    "startValue",
    "endValue",
}

RE_CALL = re.compile(r"\b([A-Za-z_][A-Za-z0-9_\.]*)\s*\(")
RE_FUNCTION_DEF = re.compile(r"^\s*function\s+([A-Za-z_][A-Za-z0-9_\.]*)\s*\(")
RE_SHARED_READ = re.compile(r"\bshared\.[A-Za-z_][A-Za-z0-9_]*")
RE_SHARED_WRITE = re.compile(r"\bshared\.[A-Za-z_][A-Za-z0-9_]*\s*=")


def build_api_catalog(*sources):
    api_names = set()
    for source in sources:
        for item in source.values():
            code = item.get("code", "")
            for match in RE_CALL.findall(code):
                api_names.add(match.split(".")[-1])
    return api_names


def validate_script(code, api_names):
    diagnostics = []
    lines = code.splitlines()

    stack = []
    for idx, raw_line in enumerate(lines, start=1):
        line = raw_line.split("--", 1)[0]
        tokens = re.findall(r"\b(function|if|for|while|repeat|end|until)\b", line)
        for token in tokens:
            if token in {"function", "if", "for", "while", "repeat"}:
                stack.append((token, idx))
            elif token == "end":
                if not stack:
                    diagnostics.append({"line": idx, "level": "error", "message": "Unexpected 'end'"})
                else:
                    stack.pop()
            elif token == "until":
                if not stack:
                    diagnostics.append({"line": idx, "level": "error", "message": "Unexpected 'until'"})
                else:
                    opener, opener_line = stack.pop()
                    if opener != "repeat":
                        diagnostics.append({"line": idx, "level": "error", "message": "'until' without matching 'repeat'"})

        for placeholder in PLACEHOLDERS:
            if placeholder in line:
                diagnostics.append({
                    "line": idx,
                    "level": "warning",
                    "message": f"Placeholder '{placeholder}' should be replaced",
                })

    for opener, opener_line in stack:
        diagnostics.append({"line": opener_line, "level": "error", "message": f"Missing end for '{opener}'"})

    function_defs = set()
    for line in lines:
        match = RE_FUNCTION_DEF.match(line)
        if match:
            func_name = match.group(1)
            function_defs.add(func_name)
            # Also add the short name (without namespace) for calls like updatePlayerThresher
            if "." in func_name:
                function_defs.add(func_name.split(".")[-1])

    # Extract custom function names (non-entry point functions defined in script)
    entry_points = {"shared.init", "server.init", "server.tick", "client.init", "client.tick"}
    custom_functions = {name for name in function_defs if name not in entry_points and "." not in name}

    required_entries = {"shared.init", "server.init", "server.tick", "client.init", "client.tick"}
    for entry in sorted(required_entries):
        if entry not in function_defs:
            diagnostics.append({
                "line": 1,
                "level": "warning",
                "message": f"Missing entry point '{entry}'",
            })

    # Track which custom functions are actually used
    used_custom_functions = set()

    for idx, raw_line in enumerate(lines, start=1):
        line = raw_line.split("--", 1)[0]
        if not line.strip():
            continue
        if RE_FUNCTION_DEF.match(line):
            continue
        for call in RE_CALL.findall(line):
            name = call.split(".")[-1]
            if name in LUA_KEYWORDS or name in COMMON_LUA_FUNCTIONS:
                continue
            if name in api_names:
                continue
            # Check if it's a custom function defined in this script
            if name in custom_functions:
                used_custom_functions.add(name)
                continue
            # Check if it's a full function definition name (like server.tick calling itself)
            if call in function_defs:
                continue
            diagnostics.append({
                "line": idx,
                "level": "warning",
                "message": f"Unknown or unsupported call '{name}'",
            })

    # Add informational notes about custom functions that are defined and used
    for func_name in sorted(used_custom_functions):
        # Find the line where the function is defined
        def_line = 1
        for idx, line in enumerate(lines, start=1):
            if RE_FUNCTION_DEF.match(line) and func_name in line:
                def_line = idx
                break
        diagnostics.append({
            "line": def_line,
            "level": "info",
            "message": f"Custom function '{func_name}' defined and used in script",
        })

    if RE_SHARED_READ.search(code) and not RE_SHARED_WRITE.search(code):
        diagnostics.append({
            "line": 1,
            "level": "warning",
            "message": "Reads from shared table without any shared writes",
        })

    for idx, raw_line in enumerate(lines, start=1):
        if "GetBodyTransform" in raw_line or "GetShapeBody" in raw_line:
            window = "\n".join(lines[max(0, idx - 4):idx + 1])
            if "IsHandleValid" not in window:
                diagnostics.append({
                    "line": idx,
                    "level": "warning",
                    "message": "Handle used without nearby IsHandleValid check",
                })

    return diagnostics
