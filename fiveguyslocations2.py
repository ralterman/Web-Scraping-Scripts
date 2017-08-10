from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import csv


count = 0
locations = []

with open('X:\Administration\Intern\Robert_Alterman\webScraping\states.txt') as f:
    lines = f.read().splitlines()

    for item in lines:
        url = 'https://order.fiveguys.com/locations/'
        url += item
        driver = webdriver.Firefox()
        driver.get(url)
        time.sleep(3)
        # driver.refresh()
        # element = WebDriverWait(driver, 10).until(
        #     lambda x: x.find_element_by_id('pac-input'))
        # time.sleep(2)
        # driver.refresh()

        try:

            addressInfo = driver.find_elements_by_xpath("//*[@class='streetaddress adr']//span[@class='street-address']")

            cityName = driver.find_elements_by_xpath("//*[@class='streetaddress adr']//span[@class='locality']")

            stateName = driver.find_elements_by_xpath("//*[@class='streetaddress adr']//span[@class='region']")

            for address, city, state in zip(addressInfo, cityName, stateName):
                address = address.text.encode('utf-8')
                city = city.text.encode('utf-8')
                state = state.text.encode('utf-8')
                info = (address, city, state)
                if info not in locations:
                    locations.append((address, city, state))
                    count += 1
                    print (address, city, state)
                else:
                    continue

            driver.quit()

        except:
            pass

    with open('fiveguysLocations.csv', 'wb') as output_file:
        location_data_writer = csv.DictWriter(output_file, fieldnames=['Address', 'City', 'State'],
                                              extrasaction='ignore', delimiter=',', quotechar='"')

        output_file.flush()
        location_data_writer.writeheader()

        for store in locations:
            location_data_writer.writerow(
                {'Address': store[0], 'City': store[1], 'State': store[2]})

print ('')
print ('There are ' + str(count) + ' locations')
print ('')