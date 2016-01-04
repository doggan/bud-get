""" CLI interface.
"""
import argparse
import bud_get
from pkg_resources import get_distribution

def main():
    VERSION = get_distribution('bud-get').version

    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help = "the input data file")
    parser.add_argument("outfile", help = "the output file")
    parser.add_argument('--version', action='version', version='v%s' % VERSION)
    args = parser.parse_args()

    in_path = args.infile
    out_path = args.outfile

    print "Processing [%s]..." % in_path
    csv_data = bud_get.filter_csv(in_path)
    bud_get.write_csv(csv_data, out_path)

if __name__ == "__main__":
    main()
