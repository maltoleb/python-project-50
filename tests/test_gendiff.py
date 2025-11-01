from pathlib import Path

from gendiff.generate_diff import generate_diff


def test_flat_json():
    base = Path('tests/test_data')
    file1 = base / 'file1.json'
    file2 = base / 'file2.json'
    expected = base / 'expected_flat.txt'
    result = generate_diff(file1, file2)
    
    with open(expected) as f:
        expected_content = f.read()
        
    assert result.strip() == expected_content.strip()


def test_flat_yaml():
    base = Path('tests/test_data')
    file1 = base / 'file1.yml'
    file2 = base / 'file2.yml'
    expected = base / 'expected_flat.txt'
    result = generate_diff(file1, file2)
    
    with open(expected) as f:
        expected_content = f.read()
    
    assert result.strip() == expected_content.strip()


def test_nested_json():
    base = Path('tests/test_data')
    file1 = base / 'file1_nested.json'
    file2 = base / 'file2_nested.json'
    expected = base / 'expected_nested.txt'
    result = generate_diff(file1, file2)

    with open(expected) as f:
        expected_content = f.read()
    
    assert result.strip() == expected_content.strip()


def test_nested_yaml():
    base = Path('tests/test_data')
    file1 = base / 'file1_nested.yml'
    file2 = base / 'file2_nested.yml'
    expected = base / 'expected_nested.txt'
    result = generate_diff(file1, file2)

    with open(expected) as f:
        expected_content = f.read()
    
    assert result.strip() == expected_content.strip()


def test_plain():
    base = Path('tests/test_data')
    file1 = base / 'file1_nested.json'
    file2 = base / 'file2_nested.json'
    expected = base / 'expected_plain.txt'
    result = generate_diff(file1, file2, 'plain')

    with open(expected) as f:
        expected_content = f.read()
    
    assert result.strip() == expected_content.strip()


def test_json():
    base = Path('tests/test_data')
    file1 = base / 'file1.json'
    file2 = base / 'file2.json'
    expected = base / 'expected_json.txt'
    result = generate_diff(file1, file2, 'json')

    with open(expected) as f:
        expected_content = f.read()

    assert result.strip() == expected_content.strip()