import argparse, json, sys
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file',
        help='JSON input file',
        type=argparse.FileType('r'),
    )
    parser.add_argument(
        '-i', '--indent',
        help='Non-negative integer indent level',
        type=int
    )
    parser.add_argument(
        '-o', '--output',
        help='Write JSON into output file',
        type=argparse.FileType('w'),
    )
    parser.add_argument(
        '-s', '--sort-keys',
        action='store_true',
        help='Sort output JSON by keys',
    )
    args = parser.parse_args()
    if not args.file:
        parser.print_usage()
        return sys.exit(EXIT_FAILURE)
    gson = json.dumps(
        json.load(args.file),
        indent=args.indent,
        sort_keys=args.sort_keys
    )
    args.file.close()
    if args.output:
        args.output.write(gson)
        args.output.write('\n')
        args.output.close()
    else:
        print(gson)
    return sys.exit(EXIT_SUCCESS)
