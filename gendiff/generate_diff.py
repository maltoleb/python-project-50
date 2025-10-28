from gendiff.parser import parse


def generate_diff(filepath1, filepath2):
    data1 = parse(filepath1)
    data2 = parse(filepath2)
    resulted_list = build_diff(data1, data2)
    return format_diff(resulted_list)

    
def build_diff(data1, data2):
    diff = []
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in keys:
        if key not in data2:
            diff.append({
                "key": key,
                "type": "removed",
                "value": data1[key]
            }
            )
        elif key not in data1:
            diff.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            }
            )
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(data1[key], data2[key])
            }
            )





    # diff_list = []
    # all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    # for key in all_keys:
    #     if key not in data2:
    #         diff_list.append(f'  - {key}: {data1[key]}')
    #     elif key not in data1:
    #         diff_list.append(f'  + {key}: {data2[key]}')
    #     elif data1[key] == data2[key]:
    #         diff_list.append(f'    {key}: {data1[key]}')
    #     else:
    #         diff_list.append(f'  - {key}: {data1[key]}')
    #         diff_list.append(f'  + {key}: {data2[key]}')
    # return diff_list


def format_diff(diff_list):
    formatted_list = '\n'.join(diff_list)
    return '{\n' + formatted_list + '\n}'