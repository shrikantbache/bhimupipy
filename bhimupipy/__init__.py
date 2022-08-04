#!/usr/bin/python

import json
import argparse
import requests
from .app import verify_upi
from .version import __version__


parser = argparse.ArgumentParser(
    description="bhimupipy: Get the details of UPI ID.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-v", "--version", action="store_true",
                    help="print the version of the package")
parser.add_argument("--upi", help="see upi datails")
args = parser.parse_args()
config = vars(args)


def start_bhimupipy(config):
    data = verify_upi(config['upi'])
    if data['result']:
        if data['data']['vpaValid']:
            data1 = {
                "result": True,
                "vpa": config['upi'],
                "vpaValid": data['data']['vpaValid'],
                "payeeAccountName": data['data']['payeeAccountName'],
                "message": "Verified UPI ID"
            }
            print(json.dumps(data1, indent=3))
        else:
            data1 = {
                "result": True,
                "vpa": config['upi'],
                "vpaValid": data['data']['vpaValid'],
                "message": "Invalid UPI ID!"
            }
            print(json.dumps(data1, indent=3))

    else:
        data1 = {
            "result": False,
            "vpa": config['upi'],
            "vpaValid": False,
            "message": "Invalid UPI ID!"
        }

        print(json.dumps(data1, indent=3))


def ExecuteBhimupiPy():
    if config['version'] == True and config['upi'] == None:
        print(__version__)
    elif config['version'] == False and config['upi'] != None:
        start_bhimupipy(config)
    else:
        parser.print_help()

if __name__ == '__main__':
    ExecuteBhimupiPy()
