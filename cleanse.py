#!/usr/bin/env python3

import os
import argparse
from lxml import etree


def traverse_nodes(root_node):
    for node in root_node:
        print(node.text)


def file_data(file_path):
    """
    Parse data from the specified file and return as a string.
    """
    data = ''
    try:
        with open(file_path, 'r') as file:
            data = file.read()
    except IOError:
        print('Error accessing file {}'.format(file_path))

    return data


def main(args):
    xml_string = ''

    if os.path.isdir(args.file_location):
        for file_name in os.listdir(args.file_location):
            if file_name.endswith('.xml'):
                xml_string = file_data(file_name)

    xml_string = file_data(args.file_location)
    # root_node = etree.fromstring(xml_string)


def parse_args():
    """
    Basic argument parsing for running the file as a script.
    """
    parser = argparse.ArgumentParser(
        description='Takes an input xml file/directory and replaces specified nodes with mock data.'
        )

    parser.add_argument(
        'file_location',
        help='File or directory to modify.'
        )

    parser.add_argument(
        'mapping_file',
        help='JSON file. Specifies functions to use when replacing xml nodes of interest.'
        )

    parser.add_argument(
        '-r',
        '--retain-original',
        action='store_false',
        help='Keep a copy of the original file. Default functionality is to alter in place.'
        )

    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_args()
    main(args)
