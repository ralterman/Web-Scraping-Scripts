from bs4 import BeautifulSoup, NavigableString, Tag
import urllib2
import csv


print ('')

html_page = urllib2.urlopen("https://regencymovies.com/")

with open('regencylinks.txt', 'r') as f:

    linklist = [line.strip() for line in f]

    names = []
    locations = []

    for link in linklist:
        req = urllib2.Request(link)
        response = urllib2.urlopen(req)
        page = response.read()
        soup = BeautifulSoup(page, 'html.parser')
        name = soup.findAll('span', attrs={'class': 'highlight'})
        for span in name:
            names.append(span.string)
            print (span.string)
        for br in soup.findAll('br'):
            next_s = br.nextSibling
            if not (next_s and isinstance(next_s, NavigableString)):
                continue
            next2_s = next_s.nextSibling
            if next2_s and isinstance(next2_s, Tag) and next2_s.name == 'br':
                text = str(next_s).strip()
                if text:
                    locations.append(next_s)
                    print (next_s)
        print ('')

    individual_locations = [locations[x:x+3] for x in xrange(0, len(locations), 3)]

    for item in individual_locations[17:]:
        del item[0]

    total = zip(names, individual_locations)

    with open('regencytheaters.csv', 'wb') as output_file:
        theater_writer = csv.DictWriter(output_file, fieldnames=['Theater Name', 'Address', 'City', 'State', 'Zip'],
                                                      extrasaction='ignore', delimiter=',', quotechar='"')

        theater_writer.writeheader()

        for regency in total:

            if regency[1][1] != 'Suite L':
                theater_writer.writerow({'Theater Name': regency[0], 'Address': regency[1][0], 'City': regency[1][1].split(',')[0],
                                         'State': (regency[1][1].split(', ')[1])[:-7], 'Zip': (regency[1][1].split(', ')[1])[-5:]})

            else:
                theater_writer.writerow({'Theater Name': regency[0], 'Address': regency[1][0] + ', ' + regency[1][1], 'City': regency[1][2].split(',')[0],
                                         'State': (regency[1][2].split(', ')[1])[:-7], 'Zip': (regency[1][2].split(', ')[1])[-5:]})
