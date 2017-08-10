import csv


# Compare Function
def findMatch(incObjectID, IncorrectStreet, IncorrectCounty, CorrectList):  # Takes a street and county and CorrectList
    for index, item in enumerate(CorrectList):  # For list in correct list
        if IncorrectStreet in item[0] and IncorrectCounty in item[1]:  # Compare
            return incObjectID, item[0], IncorrectStreet, IncorrectCounty, item[2]  # return items


def main():

    with open('RetailCountryObjectID.csv', 'r') as incorrect:
        incorrect_data_reader = csv.DictReader(incorrect, delimiter='\t', quotechar='"')

        all_incorrect = []

        for row in incorrect_data_reader:
            columnNames = row.keys()[0]  # Get the column headers from the dictionary
            columnList = columnNames.split(',')  # Make column headers into a list

            data = row.values()[0]  # Get the column values from the dictionary
            dataList = data.split(',')  # Make column values (data) into a list

            incorrect_info = []

            # Append OBJECTID, label, and county for each row to a list
            incorrect_info.append(dataList[columnList.index('OBJECTID')])
            incorrect_info.append(dataList[columnList.index('label')])
            incorrect_info.append(dataList[columnList.index('county')])

            all_incorrect.append(incorrect_info)


    with open('CorrectRetailCountryObjectID.csv', 'r') as correct:
        correct_data_reader = csv.DictReader(correct, delimiter='\t', quotechar='"')

        all_correct = []

        for row in correct_data_reader:

            columnNames2 = row.keys()[0]  # Get the column headers from the dictionary
            columnList2 = columnNames2.split(',')  # Make column headers into a list

            data2 = row.values()[0]  # Get the column values from the dictionary
            dataList2 = data2.split(',')  # Make column values (data) into a list

            correct_info = []

            # Append label, county, and Angle for each row to a list
            correct_info.append(dataList2[columnList2.index('label')])
            correct_info.append(dataList2[columnList2.index('county')])
            correct_info.append(dataList2[columnList2.index('Angle')])

            all_correct.append(correct_info)


    matches = []
    match_count = 0
    nomatch_count = 0

    # For each row in incorrect, pulls street and county into function
    for incorrect in all_incorrect:  # Access element in nested list
        incObjectID = incorrect[0]  # ObjectID in row
        incStreet = incorrect[1]  # Street in Row
        incCounty = incorrect[2]  # County in Row
        MatchResult = findMatch(incObjectID, incStreet, incCounty, all_correct)  # Function call
        if MatchResult is not None:  # If Match is found, prints matched records
            match_count += 1
            matches.append(MatchResult)  # Append all matches to a list for output file
            print "Matched:", MatchResult
        else:  # Row not matched to anything in the correct file
            nomatch_count += 1
            print "Match not found for: ", incorrect


    print ("")
    print ("----------------------------------------------------------------------------------------------")
    print ("")
    print (str(match_count) + ' rows had matches')
    print (str(nomatch_count) + ' rows had no match')
    print ("")


    with open('CorrectAngles.csv', 'wb') as output_file:
        angle_data_writer = csv.DictWriter(output_file, fieldnames=['OBJECTID', 'Angle'],
                                              extrasaction='ignore', delimiter=',', quotechar='"')

        angle_data_writer.writeheader()

        for entry in matches:
            angle_data_writer.writerow({'OBJECTID': entry[0], 'Angle': entry[4]})
            # Write row to CSV file consisting of OBJECTID from incorrect data and Angle from correct data



if __name__ == '__main__':
    main()