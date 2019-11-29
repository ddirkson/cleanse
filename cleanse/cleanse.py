#!/usr/bin/env python3

import os
import argparse
import json
from lxml import etree
from faker import Faker


class XMLCleanser():
    """
    Class to replace xml data deemed sensitive or otherwise inappropriate for public viewing.
    """

    def __init__(self, file_path, mapping_file, data_spoofer, retain_original=False):
        self._file_path = file_path
        self._data_spoofer = data_spoofer
        self._retain_original = retain_original
        self._data_cache = {}

        mapping_data = self.read_file(mapping_file)
        self._replacement_mapping = json.loads(mapping_data)


    def cleanse(self):
        """
        Given a file path, a mapping file to specify replacement functions,
        and a data spoofing class, loop through all relevant xml nodes and
        replace them as necessary before writing the results to a file.
        """
        if os.path.isdir(self._file_path):
            for file_name in os.listdir(self._file_path):
                if file_name.endswith('.xml'):
                    self._process_file(file_name)
        else:
            self._process_file(self._file_path)

        print('Done cleaning XML!')


    def _process_file(self, file_path):
        """
        Parse the xml and perform the data replacement.
        """
        xml_string = self.read_file(file_path)
        root_node = etree.fromstring(xml_string)
        self._traverse_nodes(root_node)
        self.write_file(file_path, root_node, self._retain_original)


    def _traverse_nodes(self, root_node):
        """
        Loop through each xml node and perform data replacement operation.
        """
        for node in root_node:
            if node.tag in self._replacement_mapping:
                spoof_function = self._replacement_mapping[node.tag]
                node.text = self._spoof_data(node.text, spoof_function)


    def _spoof_data(self, value, spoof_function):
        """
        Utilize our data spoofer to create a replacement value for the passed in value.
        If we've replaced this value before, return the value from the data cache instead
        so we keep things cohesive.
        """
        if value in self._data_cache:
            return self._data_cache[value]

        replacement_val = ''
        try:
            replacement_val = getattr(self._data_spoofer, spoof_function)()
        except AttributeError:
            print('[-] {} is not a valid data spoofing method for {}. ' \
                'Replacing value with empty string.'.format(
                    spoof_function,
                    self._data_spoofer.__class__
                ))

        self._data_cache[value] = replacement_val
        return replacement_val


    @staticmethod
    def write_file(file_path, root_node, retain_original=False):
        """
        Write the passed in xml to the specified file path.
        Writes to a new file if retain_original is true.
        """
        if retain_original:
            file_path = file_path.replace('.xml', '_copy.xml')

        try:
            with open(file_path, 'w+') as file:
                data = etree.tostring(root_node, encoding='unicode')
                file.write(data)
        except IOError:
            print('[-] Error writing file {}'.format(file_path))
            raise


    @staticmethod
    def read_file(file_path):
        """
        Parse data from the specified file and return as a string.
        """
        data = ''
        try:
            with open(file_path, 'r') as file:
                data = file.read()
        except IOError:
            print('[-] Error reading file {}'.format(file_path))
            raise

        return data


def cleanse_xml(file_path, mapping_file, retain_original=False):
    """
    Entry-point for the cleanse script.
    """
    data_faker = Faker()
    cleanser = XMLCleanser(file_path, mapping_file, data_faker, retain_original)
    cleanser.cleanse()


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
        action='store_true',
        help='Keep a copy of the original file. Default functionality is to alter in place.'
        )

    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_args()
    cleanse_xml(args.file_path, args.mapping_file, args.retain_original)
