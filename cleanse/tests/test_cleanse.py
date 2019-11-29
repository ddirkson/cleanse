
import os
import pytest
from cleanse import cleanse


def test_end_to_end():
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test.xml')
    mapping_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mapping.json')
    assert os.path.exists(file_path)
    assert os.path.exists(mapping_file)

    pre_data = ''
    with open(file_path, 'r') as file:
        pre_data = file.read()

    cleanse.cleanse_xml(file_path, mapping_file)
    post_data = ''
    with open(file_path, 'r') as file:
        post_data = file.read()

    assert pre_data != post_data
