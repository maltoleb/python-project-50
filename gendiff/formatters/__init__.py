from gendiff.formatters import plain, stylish


def format_diff(diff, format_name='stylish'):
    if format_name == 'stylish':
        return stylish.format_stylish(diff)
    elif format_name == 'plain':
        return plain.format_plain(diff)