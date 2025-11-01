from gendiff.formatters import json, plain, stylish


def format_diff(diff, format_name='stylish'):
    if format_name == 'stylish':
        return stylish.format_stylish(diff)
    elif format_name == 'plain':
        return plain.format_plain(diff)
    elif format_name == 'json':
        return json.format_json(diff)