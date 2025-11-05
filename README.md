### Hexlet tests and linter status

[![Actions Status](https://github.com/maltoleb/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/maltoleb/python-project-50/actions)  
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=maltoleb_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=maltoleb_python-project-50)  
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=maltoleb_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=maltoleb_python-project-50)

---

# Difference Calculator (gendiff)

**gendiff** is a command-line tool for finding differences between two files.  
It compares data structures in **JSON** and **YAML** formats and outputs the difference in several styles.  
This is the second project developed as part of the **Hexlet Python Developer** course.

---

## Tools and Technologies

- **Python 3.12+**
- **[uv](https://github.com/astral-sh/uv)** — Python package and project manager  
- **[ruff](https://docs.astral.sh/ruff/)** — linter and code formatter  
- **[pytest](https://docs.pytest.org/en/stable/)** — testing framework  
- **[PyYAML](https://pyyaml.org/)** — YAML parser and emitter for Python  
- **GitHub Actions** — continuous integration  
- **[SonarCloud](https://sonarcloud.io/)** — code quality and test coverage analysis  

---

## Installation

``` 
git clone git@github.com:maltoleb/python-project-50.git
```

````
cd python-project-50
````

`````
uv build
``````

````````
uv tool install dist/*.whl
````````

---

## Supported File Formats

- JSON (`.json`)
- YAML (`.yaml`, `.yml`)

---

## Usage

1. Place the files you want to compare inside the `tests/test_data/` directory.  
2. Run the following command, replacing `<file1>` and `<file2>` with your actual file names:

```
uv run gendiff tests/test_data/<file1> tests/test_data/<file2>
```

By default, output is shown in the **stylish** format.

To specify a different format (`plain` or `json`), use the `-f` flag.

---

### Output Examples

**Default (stylish) formatter:**
```
uv run gendiff tests/test_data/<file1> tests/test_data/<file2>
```

**Using the plain formatter:**
```
uv run gendiff -f plain tests/test_data/<file1> tests/test_data/<file2>
```

**Using the JSON formatter:**
```
uv run gendiff -f json tests/test_data/<file1> tests/test_data/<file2>
```

---

## Development and Testing

**Run linter:**
```
make lint
```

**Run tests with coverage:**
```
make test-coverage
```

---

## Asciinema Demos

- [Step 4](https://asciinema.org/a/2UZnPAYXseAaB1vzz39bwc2ZK)  
- [Step 6](https://asciinema.org/a/vyrLObXclocmPhaS6KcJvVwjb)  
- [Step 7](https://asciinema.org/a/4BfLJP9iCthsBHp3XnHg1mSN8)  
- [Step 8](https://asciinema.org/a/SVzN4cCbrF2VmwLSvPpJqcj6H)  
- [Step 9](https://asciinema.org/a/HXtTu0ZNuRxI2xdUu053nYOPP)  

---

