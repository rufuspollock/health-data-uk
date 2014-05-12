import os
import urllib

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

