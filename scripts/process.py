import os
import urllib
import csv

months = ['January', 'April', 'July', 'October']
# do some future proofing by having years in the future!
years = [2011, 2012, 2013, 2014, 2015]

def shmi_download():
    for year in years:
        for month in months:
            # data starts at October 2011
            if (year == 2011 and month != 'October'):
                continue
            url = 'https://indicators.ic.nhs.uk/download/SHMI/%s_%s/Data/SHMI.csv' % (month, year)
            dest = os.path.join('archive', 'shmi-%s-%s.csv' % (year, month.lower()))
            print('Retrieving %s' % url)
            urlfo = urllib.urlopen(url)
            code = urlfo.getcode()
            if code == 200:
                open(dest, 'w').write(urlfo.read())
            else:
                print('skipping - code: %s' % code)
                # break at this point since end of data
                break

def shmi_consolidate():
    fo = open('data/shmi.csv', 'w')

    # indicator code is always the same so we'll drop it
    fields = 'PROVIDER,PROVIDER NAME,DENOMINATOR,OBSERVED,EXPECTED,VALUE,PO_LL,PO_UL,OD_LL,OD_UL,OD_BANDING'.split(',')
    fields.insert(0, 'DATE')
    # we ignore INDICATOR CODE plus 'PO_BANDING' hence ignore for extras
    writer = csv.DictWriter(fo, lineterminator='\n', fieldnames=fields,
            extrasaction='ignore')
    writer.writeheader()

    rows = []
    for fn in [ x for x in os.listdir('archive') if x.startswith('shmi-') ]:
        fp = os.path.join('archive', fn)
        parts = fn.replace('.csv', '').split('-')
        lookup = {
                'january': '01',
                'april': '04',
                'july': '07',
                'october': '10'
                }
        date = '%s-%s-01' % (parts[1], lookup[parts[2]])
        reader = csv.DictReader(open(fp))
        for row in reader:
            # skip copyright and blank line at end of file
            # ,,,,,,,,,,,
            # "Copyright 2013, Health and Social Care Information Centre. All Rights Reserved",,,,,,,,,,,
            if row['INDICATOR_CODE'] == '':
                break
            row['DATE'] = date
            rows.append(row)

    # sort rows on date then provider
    def _cmp(row1, row2):
        if row1['DATE'] == row2['DATE']:
            return cmp(row1['PROVIDER'], row2['PROVIDER'])
        else:
            return cmp(row1['DATE'], row2['DATE'])
    rows = sorted(rows, _cmp)

    # write to output
    writer.writerows(rows)

if __name__ == '__main__':
    # shmi_download()
    shmi_consolidate()

