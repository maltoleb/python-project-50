import json


def generate_diff(filepath1, filepath2):
    data1 = read_json(filepath1)
    data2 = read_json(filepath2)
    resulted_list = build_diff(data1, data2)
    return format_diff(resulted_list)


def read_json(filepath):
    with open(filepath) as f:
        return json.load(f)
    

def build_diff(data1, data2):
    diff_list = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in all_keys:
        if key not in data2:
            diff_list.append(f'  - {key}: {data1[key]}')
        elif key not in data1:
            diff_list.append(f'  + {key}: {data2[key]}')
        elif data1[key] == data2[key]:
            diff_list.append(f'    {key}: {data1[key]}')
        else:
            diff_list.append(f'  - {key}: {data1[key]}')
            diff_list.append(f'  + {key}: {data2[key]}')
    return diff_list


def format_diff(diff_list):
    formatted_list = '\n'.join(diff_list)
    return '{\n' + formatted_list + '\n}'