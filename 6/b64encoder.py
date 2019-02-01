#! /usr/bin/env python
# coding: utf-8

import argparse
import base64

parser = argparse.ArgumentParser(description="Base64 Encoder")

parser.add_argument('--string', dest="string", type=str, default=None, help="String to Encode")

parser.add_argument('--cycle', dest="cycle", type=int, default=1, help="How Many Encode String")

args = parser.parse_args()


def b64encode(string, cycle):
    encoded_string = string
    for i in range(cycle):
        encoded_string = base64.b64encode(bytes(encoded_string, "utf-8")).decode("utf-8")
    return encoded_string


def main():
    print("Input String: {} Encode Cycle: {}".format(args.string, args.cycle))
    print("Encoded String Result:", b64encode(args.string, args.cycle))


if __name__ == '__main__':
    main()
