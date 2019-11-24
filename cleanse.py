#!/usr/bin/env python3

import argparse
from lxml import etree


def traverse_nodes(xml_string: str):
    root_node = etree.fromstring(xml_string)
    for node in root_node:
        print(node.text)


def main():
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_args()
    main(*args)
