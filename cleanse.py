#!/usr/bin/env python3

import argparse


def main():
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = parse_args()
    main(*args)
