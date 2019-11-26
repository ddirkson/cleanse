#!/usr/bin/env python3

import os
import argparse
import json
from lxml import etree


class XMLCleanser():


    def __init__(self, file_location, mapping_file, retain_original=False):
        self._file_location = file_location
        self._retain_original = retain_original

        mapping_data = self.file_data(mapping_file)
        self._replacement_mapping = json.loads(mapping_data)


    @staticmethod
    def traverse_nodes(root_node):
        """
        Loop through each xml node and perform data replacement operation
        """
        for node in root_node:
            print(node.text)


    @staticmethod
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
    cleanser = XMLCleanser(args.file_location, args.mapping_file, args.retain_original)

    # xml_string = ''
    # if os.path.isdir(args.file_location):
    #     for file_name in os.listdir(args.file_location):
    #         if file_name.endswith('.xml'):
    #             xml_string = file_data(file_name)
    #             root_node = etree.fromstring(xml_string)
    #             traverse_nodes(root_node)

    # xml_string = file_data(args.file_location)
    # root_node = etree.fromstring(xml_string)
    # traverse_nodes(root_node)


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
