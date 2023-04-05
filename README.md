# PySwissArmy

PySwissArmy is a Python utility library designed to make common programming tasks easier.
The library includes modules for working with data, files, and strings, as well as mathematical and statistical calculations.
It also includes modules for working with CSV files and Pandas dataframes.
PySwissArmy is designed to be easy to use, with a simple API and clear documentation.
Whether you're a beginner or an experienced Python developer, PySwissArmy can help you save time and simplify your code.

## Installation

You can install PySwissArmy using pip:

```
pip install pyswissarmy
```

## Usage

- read_file(file_path)
- write_file(file_path, contents)
- parse_json(json_string)
- serialize_json(data)
- current_datetime()
- class ConfigManager
- - init(self, config_file_path)
- - load_config(self)
- - save_config(self)
- - get_config(self, key, default=None)
- - set_config(self, key, value)
- class MathUtils
- - average(numbers)
- - median(numbers)
- - factorial(n)
- class StringUtils
- - reverse(string)
- - shuffle(string)
- - hash(string, algorithm='sha256')
- class DataUtils
- - flatten(nested_list)
- - transpose(matrix)
- class CSVUtils
- - read_csv(file_path)
- - write_csv(file_path, data)
- class PandasUtils
- - read_csv(file_path)
- - write_csv(file_path, data)
