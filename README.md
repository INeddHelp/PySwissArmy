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
```python
import pyswissarmy
contents = pyswissarmy.read_file('example.txt')
print(contents)
```

- write_file(file_path, contents)

Writes a string to a file
Here's an example usage:
```python
import pyswissarmy
pyswissarmy.write_file('output.txt', 'Hello World!')
```

- parse_json(json_string)

Parses a JSON string and returns a Python object
Here's an example usage:
```python
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = pyswissarmy.parse_json(json_string)
```

- serialize_json(data)

Serializes a Python object to a JSON string
Here's an example usage:
```python
data = {"name": "John", "age": 30, "city": "New York"}
json_string = pyswissarmy.serialize_json(data)
```

- current_datetime()

Returns the current date and time as a datetime object
Here's an example usage:
```python
current_time = pyswissarmy.current_datetime()
```

- class ConfigManager
```python
# Create an instance of ConfigManager with a new config file
config_manager = pyswissarmy.ConfigManager('example_config.json')
```

- - load_config(self)

Loads the configuration data from the file specified in the config_file_path attribute.
Here's an example usage:
```python
pyswissarmy.config_manager.set_config('name', 'John')
```

- - save_config(self)

Saves the configuration data to the file specified in the config_file_path attribute.
Here's an example usage:
```python
pyswissarmy.config_manager.save_config()
```

- - get_config(self, key, default=None)

Returns the value associated with the given key in the configuration data. If the key does not exist, it returns the default value, which is None by default.
Here's an example usage:
```python
name = pyswissarmy.config_manager.get_config('name')
```

### Create a new instance of ConfigManager using an existing config file
```python
existing_config_manager = pyswissarmy.ConfigManager('example_config.json')
```

- - set_config(self, key, value)

Sets the value associated with the given key in the configuration data and saves the config to the file.
Here's an example usage:
```python
name = existing_config_manager.pyswissarmyget_config('name')
```

- class MathUtils
- - average(numbers)

Computes the average of a list of numbers
Here's an example usage:
```python
numbers = [2, 4, 6, 8, 10]
average = pyswissarmy.MathUtils.average(numbers)
```

- - median(numbers)

Computes the median of a list of numbers
Here's an example usage:
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
median = pyswissarmy.MathUtils.median(numbers)
```

- - factorial(n)

Computes the factorial of a number
Here's an example usage:
```python
n = 5
factorial = pyswissarmy.MathUtils.factorial(n)
```

- class StringUtils
- - reverse(string)

Reverses a string
Here's an example usage:
```python
string = 'hello'
reversed_string = pyswissarmy.StringUtils.reverse(string)
```

- - shuffle(string)

Shuffles the characters of a string
Here's an example usage:
```python
string = 'hello'
shuffled_string = pyswissarmy.StringUtils.shuffle(string)
```

- - hash(string, algorithm='sha256')

Computes the hash value of a string using a specified algorithm
Here's an example usage:
```python
string = 'password123'
hashed_string = pyswissarmy.StringUtils.hash(string, algorithm='sha256')
```

- class DataUtils
- - flatten(nested_list)

Flattens a nested list into a single list
Here's an example usage:
```python
nested_list = [[1, 2], [3, [4, 5]], 6]
flattened_list = pyswissarmy.DataUtils.flatten(nested_list)
```

- - transpose(matrix)

Transposes a matrix (list of lists)
Here's an example usage:
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = pyswissarmy.DataUtils.transpose(matrix)
```

- class CSVUtils
- - read_csv(file_path)

Writes data to a CSV file
Here's an example usage:
```python
file_path = 'example.csv'
csv_data = pyswissarmy.CSVUtils.read_csv(file_path)
```

- - write_csv(file_path, data)

Writes data to a CSV file
Here's an example usage:
```python
file_path = 'example.csv'
data = [['Name', 'Age'], ['Alice', 25], ['Bob', 30]]
pyswissarmy.CSVUtils.write_csv(file_path, data)
```

- class PandasUtils
- - read_csv(file_path)
Reads data from a CSV file and returns it as a Pandas DataFrame
Here's an example usage:
```python
file_path = 'example.csv'
dataframe = pyswissarmy.PandasUtils.read_csv(file_path)
```

- - write_csv(file_path, data)
Writes data to a CSV file from a Pandas DataFrame
Here's an example usage:
```python
file_path = 'example.csv'
dataframe = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
pyswissarmy.PandasUtils.write_csv(file_path, dataframe)
```
