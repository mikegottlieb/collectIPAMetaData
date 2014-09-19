#!/usr/bin/env python
import json
import sys
import optparse

GENERIC_URL_SCHEMES = ["http", "https", "mailto", "sms"]

def main():
    optp = optparse.OptionParser('usage: %prog [options] file"')

    optp.add_option('-i', '--inputfile', action='store', dest='input_file', default=sys.stdin,
        help='file containing existing iHasApp scheme dictionary')
    optp.add_option('-o', '--outputfile', action='store', dest='output_file', default=sys.stdout,
        help='location to write the JSON to (default: stdout)')

    args = optp.parse_args()

    filename = str(args[0].input_file)
    mappings = json.load(open(filename, 'r'))
    for scheme in GENERIC_URL_SCHEMES:
        if mappings.has_key(scheme):
            del mappings[scheme]

    results = json.dumps(mappings, sort_keys=True)
    fo = args[0].output_file
    if isinstance(fo, str):
        fo = open(fo, 'w')
    fo.writelines(results)

if __name__ == '__main__':
    main()
