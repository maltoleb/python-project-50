def stringify(value, depth):
    # Нормализуем YAML-пустые значения ('', ' ', '\n', '\r', etc.)
    if isinstance(value, str) and value.strip() == '':
        return ''

    # Настоящие None из JSON — null
    if value is None:
        return 'null'

    if value is True:
        return 'True' if depth == 1 else 'true'
    if value is False:
        return 'False' if depth == 1 else 'false'

    if isinstance(value, dict):
        indent = ' ' * ((depth + 1) * 4)
        closing_indent = ' ' * (depth * 4)
        lines = []
        for key, val in value.items():
            child = stringify(val, depth + 1)
            # 🔥 Исправлено: если значение пустое — без пробела после двоеточия
            if child == '':
                lines.append(f"{indent}{key}:")
            else:
                lines.append(f"{indent}{key}: {child}")
        result = '\n'.join(lines)
        return f"{{\n{result}\n{closing_indent}}}"

    return str(value)


def format_stylish(diff, depth=1):  # noqa: C901
    lines = []
    indent = ' ' * (depth * 4 - 2)
    closing_indent = ' ' * ((depth - 1) * 4)

    def render_line(sign, key, value):
        # Нормализуем строки перед проверкой — обрезаем пробелы и переводы строк
        val_str = stringify(value, depth).strip()
        return (f"{indent}{sign}{key}:"
                if val_str == ''
                else f"{indent}{sign}{key}: {val_str}")

    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            nested = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent}  {key}: {nested}")
        elif node_type == 'added':
            lines.append(render_line('+ ', key, node['value']))
        elif node_type == 'removed':
            lines.append(render_line('- ', key, node['value']))
        elif node_type == 'unchanged':
            lines.append(render_line('  ', key, node['value']))
        elif node_type == 'updated':
            lines.append(render_line('- ', key, node['old_value']))
            lines.append(render_line('+ ', key, node['new_value']))

    result = '\n'.join(lines)
    return f"{{\n{result}\n{closing_indent}}}"