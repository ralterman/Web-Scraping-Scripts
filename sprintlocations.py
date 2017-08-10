from selenium import webdriver
import time
import csv


url = 'http://storelocator.sprint.com/mobile/EZ.aspx'

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

        search = driver.find_element_by_xpath('//*[@id="mainContent_LocBox"]')
        search.send_keys(item)
        findButton = driver.find_element_by_xpath('//*[@id="mainContent_Btn"]')
        findButton.click()
        time.sleep(5)

        try:

            addressInfo = driver.find_elements_by_xpath("//*[@class='res']")

            cityName = driver.find_elements_by_xpath("//*[@class='res']")

            for address, city in zip(addressInfo, cityName):
                address = address.text.encode('utf-8').split('\n')[1]
                address = address.split(',')[0]
                city = city.text.encode('utf-8').split('\n')[1]
                city = city.split(', ')[1]
                state = item[-2:]
                info = (address, city, state)
                if info not in locations:
                    locations.append((address, city, state))
                    count += 1
                    print (address, city, state)
                else:
                    continue

            driver.quit()

        except:
            driver.quit()
            pass

    with open('sprintLocations.csv', 'wb') as output_file:
        location_data_writer = csv.DictWriter(output_file, fieldnames=['Address', 'City', 'State'],
                                              extrasaction='ignore', delimiter=',', quotechar='"')

        output_file.flush()
        location_data_writer.writeheader()

        for store in locations:
            location_data_writer.writerow({'Address': store[0], 'City': store[1], 'State': store[2]})

print ('')
print ('There are ' + str(count) + ' locations')
print ('')