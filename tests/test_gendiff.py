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