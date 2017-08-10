from selenium import webdriver
import time
import csv


url = 'http://bananarepublic.gap.com/customerService/storeLocator.do?'

count = 0
locations = []

with open('X:\Administration\Intern\Robert_Alterman\webScraping\cities.txt') as f:
    lines = f.read().splitlines()

    for item in lines:
        print (item)
        driver = webdriver.Firefox()
        driver.get(url)
        time.sleep(5)

        try:

            closeButton = driver.find_element_by_class_name('optly-modal-close')
            if closeButton.is_displayed():
                closeButton.click()

        except:
            pass

        time.sleep(5)

        search = driver.find_element_by_id('addressSearch')
        search.send_keys(item)
        findButton = driver.find_element_by_id('adressSearchButton')
        findButton.click()
        time.sleep(5)

        try:

            addressInfo = driver.find_elements_by_class_name("addressLine1")

            cityName = driver.find_elements_by_class_name("cityName")

            stateName = driver.find_elements_by_class_name("stateProvinceCode")

            zipCode = driver.find_elements_by_class_name("postalCode")

            storeType = driver.find_elements_by_class_name("storeType")

            for address, city, state, zips, types in zip(addressInfo, cityName, stateName, zipCode, storeType):
                address = address.text.encode('utf-8')
                city = city.text.encode('utf-8')
                state = state.text.encode('utf-8')
                zips = str(zips.text.encode('utf-8'))
                types = types.text.encode('utf-8')
                info = (address, city, state, zips, types)
                if info not in locations:
                    locations.append((address, city, state, zips, types))
                    count += 1
                    print (address, city, state, zips, types)
                else:
                    continue

            driver.quit()

        except:
            pass

    with open('bananarepublicLocations.csv', 'ab') as output_file:
        location_data_writer = csv.DictWriter(output_file, fieldnames=['Address', 'City', 'State', 'Zip', 'Store Type'],
                                              extrasaction='ignore', delimiter=',', quotechar='"')

        output_file.flush()
        location_data_writer.writeheader()

        for store in locations:
            location_data_writer.writerow(
                {'Address': store[0], 'City': store[1], 'State': store[2], 'Zip': store[3], 'Store Type': store[4]})

print ('')
print ('There are ' + str(count) + ' locations')
print ('')