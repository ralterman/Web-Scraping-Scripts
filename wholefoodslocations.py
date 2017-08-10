from selenium import webdriver
import time
import csv


url = 'http://www.wholefoodsmarket.com/stores/list'

count = 0
locations = []

with open('X:\Administration\Intern\Robert_Alterman\webScraping\cities.txt') as f:
    lines = f.read().splitlines()

    for item in lines:
        print (item)
        driver = webdriver.Firefox()
        driver.get(url)

        # closeButton = driver.find_element_by_class_name('optly-modal-close')
        # if closeButton.is_displayed():
        #     closeButton.click()
        time.sleep(5)

        search = driver.find_element_by_id('edit-field-geo-data-latlon-address')
        search.send_keys(item)
        findButton = driver.find_element_by_id('edit-submit-store-lookup-by-address')
        findButton.click()
        time.sleep(5)

        try:

            addressInfo = driver.find_elements_by_class_name("thoroughfare")

            cityName = driver.find_elements_by_class_name("locality")

            stateName = driver.find_elements_by_class_name("state")

            zipCode = driver.find_elements_by_class_name("postal-code")

            for address, city, state, zips in zip(addressInfo, cityName, stateName, zipCode):
                address = address.text.encode('utf-8')
                city = city.text.encode('utf-8')
                state = state.text.encode('utf-8')
                zips = str(zips.text.encode('utf-8'))
                info = (address, city, state, zips)
                if info not in locations:
                    locations.append((address, city, state, zips))
                    count += 1
                    print (address, city, state, zips)
                else:
                    continue

            driver.quit()

        except:
            pass

    with open('wholefoodsLocations.csv', 'wb') as output_file:
        location_data_writer = csv.DictWriter(output_file, fieldnames=['Address', 'City', 'State', 'Zip'],
                                              extrasaction='ignore', delimiter=',', quotechar='"')

        output_file.flush()
        location_data_writer.writeheader()

        for store in locations:
            location_data_writer.writerow({'Address': store[0], 'City': store[1], 'State': store[2], 'Zip': store[3]})

print ('')
print ('There are ' + str(count) + ' locations')
print ('')