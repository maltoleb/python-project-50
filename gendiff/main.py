from gendiff import cli
import json


def main():
    args = cli.parse_args()
    data1 = json.load(open(args.first_file))
    data2 = json.load(open(args.second_file))
    print(data1)
    print(data2)


if __name__ == '__main__':
    main()