from selenium import webdriver
import time
import csv


url = 'https://www.soul-cycle.com/studios/all/'

count = 0
locations = []

driver = webdriver.Firefox()
driver.get(url)

time.sleep(3)

try:

    addressInfo = driver.find_elements_by_xpath("//*[@class='info-cc']//span[@class='street']")

    cityName = driver.find_elements_by_xpath("//*[@class='info-cc']//span[@class='street']")

    stateName = driver.find_elements_by_xpath("//*[@class='info-cc']//span[@class='street']")

    zipCode = driver.find_elements_by_xpath("//*[@class='info-cc']//span[@class='street']")

    for address, city, state, zips in zip(addressInfo, cityName, stateName, zipCode):
        address = address.text.encode('utf-8').split('\n')[0]
        city = (city.text.encode('utf-8').split('\n')[1]).split()[:-2]
        city = " ".join(city)[:-1]
        state = state.text.encode('utf-8')[-8:-6]
        zips = str(zips.text.encode('utf-8').split()[-1])
        info = (address, city, state, zips)
        if ('Toronto, O' in city) or ('Vancouver, B' in city):
            continue
        else:
            if info not in locations:
                locations.append((address, city, state, zips))
                count += 1
                print (address, city, state, zips)
            else:
                continue

    driver.quit()

except:
    pass

with open('soulcycleLocations.csv', 'wb') as output_file:
    location_data_writer = csv.DictWriter(output_file, fieldnames=['Address', 'City', 'State', 'Zip'],
                                          extrasaction='ignore', delimiter=',', quotechar='"')

    output_file.flush()
    location_data_writer.writeheader()

    for store in locations:
        location_data_writer.writerow({'Address': store[0], 'City': store[1], 'State': store[2], 'Zip': store[3]})

print ('')
print ('There are ' + str(count) + ' locations')
print ('')