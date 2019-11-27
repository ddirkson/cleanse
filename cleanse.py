#!/usr/bin/env python3

import os
import argparse
import json
from lxml import etree


class XMLCleanser():


    def __init__(self, file_path, mapping_file, retain_original=False):
        self._file_path = file_path
        self._retain_original = retain_original

        mapping_data = self.file_data(mapping_file)
        self._replacement_mapping = json.loads(mapping_data)



    def cleanse_xml(self):
        xml_string = ''
        if os.path.isdir(args.file_path):
            for file_name in os.listdir(args.file_path):
                if file_name.endswith('.xml'):
                    xml_string = self.file_data(file_name)
                    root_node = etree.fromstring(xml_string)
                    self.traverse_nodes(root_node)

        xml_string = self.file_data(self._file_path)
        root_node = etree.fromstring(xml_string)
        self.traverse_nodes(root_node)


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
    cleanser = XMLCleanser(args.file_path, args.mapping_file, args.retain_original)
    cleanser.cleanse_xml()


def parse_args():
    """
    Basic argument parsing for running the file as a script.
    """
    parser = argparse.ArgumentParser(
        description='Takes an input xml file/directory and replaces specified nodes with mock data.'
        )

    parser.add_argument(
        'file_path',
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
