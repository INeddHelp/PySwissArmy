import os
import datetime
import json
import random
import hashlib
import csv
import pandas as pd


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def write_file(file_path, contents):
    with open(file_path, 'w') as f:
        f.write(contents)


def parse_json(json_string):
    return json.loads(json_string)


def serialize_json(data):
    return json.dumps(data)


def current_datetime():
    return datetime.datetime.now()


class ConfigManager:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config_data = {}

        if os.path.exists(config_file_path):
            self.load_config()
        else:
            self.save_config()

    def load_config(self):
        config_string = read_file(self.config_file_path)
        self.config_data = parse_json(config_string)

    def save_config(self):
        config_string = serialize_json(self.config_data)
        write_file(self.config_file_path, config_string)

    def get_config(self, key, default=None):
        return self.config_data.get(key, default)

    def set_config(self, key, value):
        self.config_data[key] = value
        self.save_config()


class MathUtils:
    @staticmethod
    def average(numbers):
        return sum(numbers) / len(numbers)

    @staticmethod
    def median(numbers):
        sorted_numbers = sorted(numbers)
        mid = len(numbers) // 2
        if len(numbers) % 2 == 0:
            return (sorted_numbers[mid-1] + sorted_numbers[mid]) / 2
        else:
            return sorted_numbers[mid]

    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * MathUtils.factorial(n-1)


class StringUtils:
    @staticmethod
    def reverse(string):
        return string[::-1]

    @staticmethod
    def shuffle(string):
        letters = list(string)
        random.shuffle(letters)
        return ''.join(letters)

    @staticmethod
    def hash(string, algorithm='sha256'):
        hash_func = getattr(hashlib, algorithm)
        return hash_func(string.encode()).hexdigest()


class DataUtils:
    @staticmethod
    def flatten(nested_list):
        flattened = []
        for item in nested_list:
            if isinstance(item, list):
                flattened.extend(DataUtils.flatten(item))
            else:
                flattened.append(item)
        return flattened

    @staticmethod
    def transpose(matrix):
        return [list(row) for row in zip(*matrix)]


class CSVUtils:
    @staticmethod
    def read_csv(file_path):
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            return [row for row in reader]

    @staticmethod
    def write_csv(file_path, data):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)


class PandasUtils:
    @staticmethod
    def read_csv(file_path):
        return pd.read_csv(file_path)

    @staticmethod
    def write_csv(file_path, data):
        data.to_csv(file_path, index=False)
        