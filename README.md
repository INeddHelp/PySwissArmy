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

Reads the contents of a file and returns it as a string
Here's an example usage:

```
from pyswissarmy import *
contents = read_file('example.txt')
print(contents)
```

- write_file(file_path, contents)

Writes a string to a file
Here's an example usage:
```
write_file('output.txt', 'Hello World!')
```

- parse_json(json_string)

Parses a JSON string and returns a Python object
Here's an example usage:
```

```

- serialize_json(data)

Serializes a Python object to a JSON string
Here's an example usage:
```

```

- current_datetime()

Returns the current date and time as a datetime object
Here's an example usage:
```

```

- class ConfigManager
- - load_config(self)

Loads the configuration data from the file specified in the config_file_path attribute.
Here's an example usage:
```

```

- - save_config(self)

Saves the configuration data to the file specified in the config_file_path attribute.
Here's an example usage:
```

```

- - get_config(self, key, default=None)

Returns the value associated with the given key in the configuration data. If the key does not exist, it returns the default value, which is None by default.
Here's an example usage:
```

```
- - set_config(self, key, value)

Sets the value associated with the given key in the configuration data and saves the config to the file.
Here's an example usage:
```

```

- class MathUtils
- - average(numbers)

Computes the average of a list of numbers
Here's an example usage:
```

```

- - median(numbers)

Computes the median of a list of numbers
Here's an example usage:
```

```

- - factorial(n)

Computes the factorial of a number
Here's an example usage:

```

```

- class StringUtils
- - reverse(string)

Reverses a string
Here's an example usage:
```

```

- - shuffle(string)

Shuffles the characters of a string
Here's an example usage:
```

```

- - hash(string, algorithm='sha256')

Computes the hash value of a string using a specified algorithm
Here's an example usage:
```

```

- class DataUtils
- - flatten(nested_list)

Flattens a nested list into a single list
Here's an example usage:
```

```

- - transpose(matrix)

Transposes a matrix (list of lists)
Here's an example usage:
```

```

- class CSVUtils
- - read_csv(file_path)

Writes data to a CSV file
Here's an example usage:
```

```

- - write_csv(file_path, data)

Writes data to a CSV file
Here's an example usage:
```

```

- class PandasUtils
- - read_csv(file_path)
```

```

Reads data from a CSV file and returns it as a Pandas DataFrame
Here's an example usage:
```

```

- - write_csv(file_path, data)
Writes data to a CSV file from a Pandas DataFrame
Here's an example usage:
```

```
