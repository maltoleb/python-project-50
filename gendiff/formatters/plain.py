def stringify(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
    

def format_plain(diff, path=''):
    lines = []
    for node in diff:
        key = node['key']
        node_type = node['type']
        full_path = f"{path}.{key}" if path else key
        match node_type:
            case 'nested':
                nested = format_plain(node['children'], full_path)
                lines.extend(nested.split('\n'))
            case 'added':
                value = stringify(node['value'])
                added = f"Property '{full_path}' was added with value: {value}"
                lines.append(added)
            case 'removed':
                removed = f"Property '{full_path}' was removed"
                lines.append(removed)
            case 'unchanged':
                pass
            case 'updated':
                old_value = stringify(node['old_value'])
                new_value = stringify(node['new_value'])
                updated = (
                    f"Property '{full_path}' was updated. "
                    f"From {old_value} to {new_value}"
                )
                lines.append(updated)
    return "\n".join(lines)
