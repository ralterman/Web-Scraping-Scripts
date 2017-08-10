from selenium import webdriver
import time
import csv


url = 'https://stores.jcrew.com/?'

major_cities = ['New York, NY', 'Chicago, IL', 'Seattle, WA', 'Portland, OR', 'Los Angeles, CA', 'San Francisco, CA', 'Dallas, TX', 'Denver, CO', 'Memphis, TN', 'Miami, FL',
                'Phoenix, AZ', 'New Orleans, LA', 'Atlanta, GA', 'Kansas City, MO', 'Minneapolis, MN', 'Charlotte, NC', 'Baltimore, MD', 'Pittsburgh, PA', 'Detroit, MI',
                'Buffalo, NY', 'Boston, MA', 'Portland, ME', 'Jacksonville, FL', 'Albuquerque, NM', 'Salt Lake City, UT', 'Las Vegas, NV', 'Indianapolis, IN', 'Columbus, OH', 'Helena, MT',
                'Anchorage, AK', 'Honolulu, HI', 'Birmingham, AL', 'San Antonio, TX', 'Oklahoma City, OK', 'Louisville, KY', 'Richmond, VA', 'Washington, DC']

count = 0
locations = []

for city in major_cities:
    driver = webdriver.Firefox()
    driver.get(url)

    # closeButton = driver.find_element_by_class_name('optly-modal-close')
    # if closeButton.is_displayed():
    #     closeButton.click()
    time.sleep(5)

    search = driver.find_element_by_xpath('//*[@id="bwt-q"]')
    search.send_keys(city)
    findButton = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div/div/div/button[2]/span[1]')
    findButton.click()
    time.sleep(3)

    showMore = driver.find_element_by_xpath('//*[@id="show_more_link"]')
    while showMore.is_displayed():
        driver.execute_script("arguments[0].click();", showMore)
        time.sleep(2)

    try:

        addressInfo = driver.find_elements_by_xpath("//*[@class='bwt-store-address']//*[@itemprop='streetAddress'][1]")

        cityName = driver.find_elements_by_xpath("//*[@class='bwt-store-address-line']//span[@itemprop='addressLocality']")

        stateName = driver.find_elements_by_xpath("//*[@class='bwt-store-address-line']//span[@itemprop='addressRegion']")

        zipCode = driver.find_elements_by_xpath("//*[@class='bwt-store-address-line']//span[@itemprop='postalCode']")

        phoneNum = driver.find_elements_by_xpath("//*[@class='bwt-show-for-medium-up']//span[@itemprop='telephone']")

        for address, city, state, zips, phone in zip(addressInfo, cityName, stateName, zipCode, phoneNum):
            address = address.text.encode("utf-8")
            city = city.text.encode("utf-8")[:-1]
            state = state.text.encode("utf-8")
            zips = str(zips.text.encode("utf-8"))
            phone = str(phone.text.encode("utf-8"))
            info = (address, city, state, zips, phone)
            if info not in locations:
                locations.append((address, city, state, zips, phone))
                count += 1
                print (address, city, state, zips, phone)
            else:
                continue

        driver.quit()

    except:
        pass

    with open('jcrewLocations.csv', 'wb') as output_file:
        location_data_writer = csv.DictWriter(output_file, fieldnames=['Address', 'City', 'State', 'Zip', 'Phone'],
                                              extrasaction='ignore', delimiter=',', quotechar='"')

        location_data_writer.writeheader()

        for store in locations:
            location_data_writer.writerow({'Address': store[0], 'City': store[1], 'State': store[2], 'Zip': store[3], 'Phone': store[4]})

print ('')
print ('There are ' + str(count) + ' locations')
print ('')