def stringify(value, depth):
    if value == '':
        return ' '
    if value is True:
        return 'True' if depth == 1 else 'true'
    if value is False:
        return 'False' if depth == 1 else 'false'
    if value is None:
        return 'None' if depth == 1 else 'null'

    if isinstance(value, dict):
        indent = ' ' * ((depth + 1) * 4)
        closing_indent = ' ' * (depth * 4)
        lines = []
        for key, val in value.items():
            lines.append(f"{indent}{key}: {stringify(val, depth + 1)}")
        result = '\n'.join(lines)
        return f"{{\n{result}\n{closing_indent}}}"

    return str(value)


def format_stylish(diff, depth=1):  # noqa: C901
    lines = []
    indent = ' ' * (depth * 4 - 2)
    closing_indent = ' ' * ((depth - 1) * 4)

    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            nested = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}  {key}: {nested}")

        elif node_type == 'added':
            val = stringify(node['value'], depth)
            if val == ' ':
                lines.append(f"{indent}+ {key}:")
            else:
                lines.append(f"{indent}+ {key}: {val}")

        elif node_type == 'removed':
            val = stringify(node['value'], depth)
            if val == ' ':
                lines.append(f"{indent}- {key}:")
            else:
                lines.append(f"{indent}- {key}: {val}")

        elif node_type == 'unchanged':
            val = stringify(node['value'], depth)
            if val == ' ':
                lines.append(f"{indent}  {key}:")
            else:
                lines.append(f"{indent}  {key}: {val}")

        elif node_type == 'updated':
            old_val = stringify(node['old_value'], depth)
            new_val = stringify(node['new_value'], depth)

            if old_val == ' ':
                lines.append(f"{indent}- {key}:")
            else:
                lines.append(f"{indent}- {key}: {old_val}")

            if new_val == ' ':
                lines.append(f"{indent}+ {key}:")
            else:
                lines.append(f"{indent}+ {key}: {new_val}")

    result = '\n'.join(lines)
    return f"{{\n{result}\n{closing_indent}}}"