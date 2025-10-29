def stringify(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f"    {key}: {stringify(val)}")
        result = "\n".join(lines)
        return f"{{\n{result}\n}}"

    
def format_stylish(diff, depth = 1):
    lines = []
    indent = ' '*(depth*4-2)
    for node in diff:
        if node['type'] == 'nested':
            nested_value = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}  {node['key']}: {nested_value}")
        elif node['type'] == 'added':
            added_line = f"{indent}+ {node['key']}: {stringify(node['value'], depth + 1)}"
            lines.append(added_line)
        elif node['type'] == 'removed':
            removed_line = f"{indent}- {node['key']}: {stringify(node['value'], depth + 1)}"
            lines.append(removed_line)        
        elif node['type'] == 'unchanged':
            unchanged_line = f"{indent}  {node['key']}: {stringify(node['value'], depth + 1)}"
            lines.append(unchanged_line)
        elif node['type'] == 'updated':
            updated_line1 = f"{indent}- {node['key']}: {stringify(node['old_value'], depth + 1)}"
            updated_line2 = f"{indent}+ {node['key']}: {stringify(node['new_value'], depth + 1)}"
            lines.append(updated_line1)
            lines.append(updated_line2)
    result_line = '\n'.join(lines)
    return f"{{\n{result_line}\n}}"