from project import store_database
from project import open_database
from project import filter_data
import pytest


class test:
    def __init__(self):
        self.database = []


array = []


def test_store_database():
    assert store_database(array) == "Database Stored"
    assert store_database() == "Database Not Found"


def test_open_database():
    assert open_database() == "Class Not Found, Database Cant Be Loaded"
    engine = test()
    assert open_database(engine) == "Database Opened"


def test_filter_data():
    assert filter_data() == "Values Not Found"
    filtered_names, filtered_vectors = filter_data(0, array)
    assert filtered_names == []  # this is empty in this case cause array is empty
    assert filtered_vectors == []  # this is empty in this case cause array is empty
