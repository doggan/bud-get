""" Budget utilities.
"""
import csv

def _reader_filter(entries, *keys):
    """ Perform filtering of dictionary keys, returning an interator.
    """
    for entry in entries:
        yield dict((k, entry[k]) for k in keys)

FILTER_COLUMNS = ('Type', 'Trans Date', 'Description', 'Amount')

def filter_csv(in_file):
    """ Perform filter / sorting operations on CSV data.
    """
    results = []

    with open(in_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in _reader_filter(reader, *FILTER_COLUMNS):
            # Skip payments.
            if row['Type'] == 'Payment':
                continue
            # More filtering.
            row.pop('Type', None)

            # Strip the negative sign.
            amount = row['Amount']
            if len(amount) > 0 and amount[0] == '-':
                row['Amount'] = amount[1:]

            results.append(row)

    # Sort by transaction date and amount (ascending).
    results = sorted(results, key=lambda x:\
        # Sort by year.
        (x['Trans Date'][-4:],\
        # Sort by month/day.
        x['Trans Date'][:-4],\
        # Sort by amount.
        float(x['Amount'])))

    return results

def write_csv(csv_data, out_file):
    """ Write CSV data (rows of dicts) to an output file.
    """
    if len(csv_data) <= 0:
        print "No data to write."
        return

    print "Writing %s" % out_file

    with open(out_file, 'w') as csvfile:
        fieldnames = csv_data[0].keys()

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in csv_data:
            writer.writerow(row)
