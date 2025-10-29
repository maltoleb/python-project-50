def stringify(value, depth):
    if value == '':
        return ''
    if value is True or value == 'True':
        return 'true'
    if value is False or value == 'False':
        return 'false'
    if value is None or value == 'None':
        return 'null'
    if isinstance(value, dict):
        indent = ' ' * (depth * 4)
        closing_indent = ' ' * ((depth - 1) * 4)
        lines = []
        for key, val in value.items():
            lines.append(f"{indent}{key}: {stringify(val, depth + 1)}")
        result = "\n".join(lines)
        return f"{{\n{result}\n{closing_indent}}}"
    return str(value)


def format_stylish(diff, depth=1):
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
            lines.append(f"{indent}+ {key}: {stringify(node['value'], depth + 1)}")
        elif node_type == 'removed':
            lines.append(f"{indent}- {key}: {stringify(node['value'], depth + 1)}")
        elif node_type == 'unchanged':
            lines.append(f"{indent}  {key}: {stringify(node['value'], depth + 1)}")
        elif node_type == 'updated':
            lines.append(f"{indent}- {key}: {stringify(node['old_value'], depth + 1)}")
            lines.append(f"{indent}+ {key}: {stringify(node['new_value'], depth + 1)}")

    result = "\n".join(lines)
    return f"{{\n{result}\n{closing_indent}}}"