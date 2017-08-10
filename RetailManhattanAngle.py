import csv


def main():

    # Read in input file
    with open('RetailManhattanAngle.csv', 'r') as input_file:
        retail_data_reader = csv.DictReader(input_file, delimiter = '\t', quotechar = '"')
        # Create dictionary of file rows where column headers are keys and row data are values

        row_count = 0
        output = []

        for row in retail_data_reader:

            columnNames = row.keys()[0]  # Get the column headers from the dictionary
            columnList = columnNames.split(',')  # Make column headers into a list

            data = row.values()[0]  # Get the column values from the dictionary
            dataList = data.split(',')  # Make column values (data) into a list

            streetInfo = []

            # Append OBJECTID, St_label, and StreetName for each row to a list
            streetInfo.append((columnList[columnList.index('OBJECTID')], dataList[columnList.index('OBJECTID')]))
            streetInfo.append((columnList[columnList.index('St_label')], dataList[columnList.index('St_label')]))
            streetInfo.append((columnList[columnList.index('StreetName')], dataList[columnList.index('StreetName')]))
            streetInfo.append((columnList[columnList.index('Labelside')], dataList[columnList.index('Labelside')]))

            if streetInfo[1][1] != streetInfo[2][1]:  # Check to see if St_label and StreetName match

                # Control for street suffixes (i.e., Street = St) and unique instances:

                if 'Pl' in streetInfo[2][1][-2:]:
                    if streetInfo[1][1] == 'Franklin Street' and streetInfo[2][1] == 'Franklin Pl':
                        continue
                    corrected = streetInfo[2][1][-2:].replace('Pl', 'Place')  # (i.e., Park Pl --> Park Place)
                    if streetInfo[1][1] != streetInfo[2][1][0:-2]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Cir' in streetInfo[2][1][-3:]:
                    corrected = streetInfo[2][1][-3:].replace('Cir', 'Circle')
                    if streetInfo[1][1] != streetInfo[2][1][0:-3]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Sq' in streetInfo[2][1][-2:]:
                    corrected = streetInfo[2][1][-2:].replace('Sq', 'Square')
                    if streetInfo[1][1] != streetInfo[2][1][0:-2]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Ln' in streetInfo[2][1][-2:]:
                    corrected = streetInfo[2][1][-2:].replace('Ln', 'Lane')
                    if streetInfo[1][1] != streetInfo[2][1][0:-2]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Ter' in streetInfo[2][1][-3:]:
                    corrected = streetInfo[2][1][-3:].replace('Ter', 'Terrace')
                    if streetInfo[1][1] != streetInfo[2][1][0:-3]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Plz' in streetInfo[2][1][-3:]:
                    corrected = streetInfo[2][1][-3:].replace('Plz', 'Plaza')
                    if streetInfo[1][1] != streetInfo[2][1][0:-3]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Blvd' in streetInfo[2][1][-4:]:
                    if streetInfo[1][1] == 'Frederick Douglass BoulevardFrederick Do' and streetInfo[2][1] == 'Frederick Douglass Blvd':
                        continue
                    corrected = streetInfo[2][1][-4:].replace('Blvd', 'Boulevard')
                    if streetInfo[1][1] != streetInfo[2][1][0:-4]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'St' in streetInfo[2][1][-2:]:
                    if streetInfo[1][1] == '51th Street' and streetInfo[2][1] == 'E 51st St':
                        continue
                    if streetInfo[1][1] == 'Bleeker Street' and streetInfo[2][1] == 'Bleecker St':
                        continue
                    if streetInfo[1][1] == '51th Street' and streetInfo[2][1] == 'E 51st St':
                        continue
                    if streetInfo[1][1] == 'Cornella Street' and streetInfo[2][1] == 'Cornelia St':
                        continue
                    if streetInfo[1][1] == 'Mac Dougal Street' and streetInfo[2][1] == 'MacDougal St':
                        continue
                    if streetInfo[1][1] == '116 Street' and streetInfo[2][1] == 'W 116th St':
                        continue
                    if streetInfo[1][1] == '41 Street' and streetInfo[2][1] == 'W 41st St':
                        continue
                    if streetInfo[1][1] == 'West 111 Street' and streetInfo[2][1] == 'W 111th St':
                        continue
                    if streetInfo[1][1] == 'West 113 Street' and streetInfo[2][1] == 'W 113th St':
                        continue
                    if streetInfo[1][1] == 'West 115 Street' and streetInfo[2][1] == 'W 115th St':
                        continue
                    if streetInfo[1][1] == 'West 121 Street' and streetInfo[2][1] == 'W 121st St':
                        continue
                    if streetInfo[1][1] == 'West 122 Street' and streetInfo[2][1] == 'W 122nd St':
                        continue

                    corrected = streetInfo[2][1][-2:].replace('St', 'Street')
                    if streetInfo[1][1].lower() != (streetInfo[2][1][0:-2]+corrected).lower():
                        if streetInfo[1][1].lower() not in (streetInfo[2][1][0:-2]+corrected).lower():  # i.e., 14th Street = W 14th Street
                            if streetInfo[1][1] == 'Thirteenth Street' and streetInfo[2][1] == 'W 13th St':
                                continue
                            elif streetInfo[1][1] == 'Eighth Street' and (streetInfo[2][1] == 'W 8th St' or streetInfo[2][1] == 'E 8th St'):
                                continue
                            elif len(streetInfo[2][1].split()) > 2:  # Control for instances such as North Moore Street = N Moore Street
                                if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-2]+corrected).split()[1:]):
                                    continue
                                else:
                                    row_count += 1
                                    output.append(streetInfo)
                                    print (streetInfo)
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                elif 'Ave' in streetInfo[2][1][-3:]:
                    if streetInfo[1][1] == 'St. Nicholas Avenue' and streetInfo[2][1] == 'St Nicholas Ave':
                        continue
                    corrected = streetInfo[2][1][-3:].replace('Ave', 'Avenue')

                    # Make all avenue names be equal to their numerical values (i.e., Second Avenue = 2nd Avenue)
                    if streetInfo[1][1] != streetInfo[2][1][0:-3]+corrected:
                        if streetInfo[1][1] == 'First Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '1st Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif streetInfo[1][1] == 'Second Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '2nd Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif streetInfo[1][1] == 'Third Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '3rd Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif streetInfo[1][1] == 'Fourth Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '4th Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif streetInfo[1][1] == 'Fifth Avenue' or streetInfo[1][1] == 'FIfth Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '5th Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif streetInfo[1][1] == 'SixthAvenue' or streetInfo[1][1] == 'Sixth Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '6th Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif streetInfo[1][1] == 'Seventh Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '7th Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif streetInfo[1][1] == 'Eighth Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '8th Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif streetInfo[1][1] == 'Ninth Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '9th Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif streetInfo[1][1] == 'Tenth Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '10th Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif streetInfo[1][1] == 'Eleventh Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '11th Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif streetInfo[1][1] == 'Twelfth Avenue':
                            if streetInfo[2][1][0:-3]+corrected != '12th Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        elif len(streetInfo[2][1].split()) > 2:  # Control for instances such as West End Avenue = W End Avenue
                            if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-3] + corrected).split()[1:]):
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)

                        else:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)

                elif 'Ave S' in streetInfo[2][1][-5:]:  # Avenue S = Avenue
                    corrected = streetInfo[2][1][-5:].replace('Ave S', 'Avenue')
                    if streetInfo[1][1] != streetInfo[2][1][0:-5] + corrected:
                        if streetInfo[1][1] == 'Seventh Avenue':
                            if streetInfo[2][1][0:-5]+corrected != '7th Avenue':
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                        else:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)

                # Control for certain unique instances
                elif streetInfo[1][1] == 'Greenwich Street' and streetInfo[2][1] == 'Greenwich Mews':
                    continue

                elif streetInfo[1][1] == 'Union Square' and streetInfo[2][1] == 'Union Sq E':
                    continue

                elif len(streetInfo[2][1].split()) >= 2:  # Control for instances such as West Broadway = W Broadway
                    if (streetInfo[1][1].split())[1:] == (streetInfo[2][1]).split()[1:]:
                        continue
                    else:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                else:
                    row_count += 1
                    output.append(streetInfo)
                    print (streetInfo)

            else:
                continue

        # Create output file
        with open('RetailManhattanObjectID.csv', 'wb') as output_file:
            objectID_data_writer = csv.DictWriter(output_file, fieldnames=['OBJECTID', 'St_label', 'StreetName', 'Labelside'],
                                                  extrasaction='ignore', delimiter=',', quotechar='"')

            objectID_data_writer.writeheader()

            for entry in output:
                objectID_data_writer.writerow({'OBJECTID':entry[0][1], 'St_label':entry[1][1], 'StreetName':entry[2][1], 'Labelside':entry[3][1]})
                # Write row to CSV file consisting of OBJECTID, St_label, and StreetName for incorrect data


    print ("")
    print ("-----------------------------")
    print ("")
    print (str(row_count) + " labels did not match")
    print ("")


if __name__ == '__main__':
    main()