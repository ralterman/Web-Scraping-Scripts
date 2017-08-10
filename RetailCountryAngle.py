import csv


def main():

    # Read in input file
    with open('MapInfo_NoCA_Joined.csv', 'r') as input_file:
        retail_data_reader = csv.DictReader(input_file, delimiter='\t', quotechar='"')
        # Create dictionary of file rows where column headers are keys and row data are values

        row_count = 0
        output = []

        for row in retail_data_reader:

            columnNames = row.keys()[0]  # Get the column headers from the dictionary
            columnList = columnNames.split(',')  # Make column headers into a list

            data = row.values()[0]  # Get the column values from the dictionary
            dataList = data.split(',')  # Make column values (data) into a list

            streetInfo = []

            # Append OBJECTID, label, StreetNa_1, county, labelDirec, and Angle for each row to a list
            streetInfo.append((columnList[columnList.index('OBJECTID')], dataList[columnList.index('OBJECTID')]))
            streetInfo.append((columnList[columnList.index('label')], dataList[columnList.index('label')]))
            streetInfo.append((columnList[columnList.index('StreetNa_1')], dataList[columnList.index('StreetNa_1')]))
            streetInfo.append((columnList[columnList.index('county')], dataList[columnList.index('county')]))
            streetInfo.append((columnList[columnList.index('labelDirec')], dataList[columnList.index('labelDirec')]))
            streetInfo.append((columnList[columnList.index('Angle')], dataList[columnList.index('Angle')]))

            if streetInfo[1][1] != streetInfo[2][1]:  # Check to see if label and StreetNa_1 match

                # Control for street suffixes (i.e., Street = St) and unique instances:
                # Unique cases are accounted for at the beginning of each conditional statement

                if 'Pl' in streetInfo[2][1][-2:]:
                    if streetInfo[1][1] == 'Franklin Street' and streetInfo[2][1] == 'Franklin Pl':
                        continue
                    if streetInfo[1][1] == 'Walton Street' and streetInfo[2][1] == 'E Walton Pl':
                        continue
                    if streetInfo[1][1] == 'Delware Place' and streetInfo[2][1] == 'E Delaware Pl':
                        continue
                    corrected = streetInfo[2][1][-2:].replace('Pl', 'Place')  # (i.e., Park Pl --> Park Place)
                    if len(streetInfo[2][1].split()) > 2:  # Control for instances such as North Park Place = N Park Pl
                        if len(streetInfo[1][1].split()) > 2:
                            if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-2] + corrected).split()[1:]):
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                        else:
                            if (streetInfo[1][1].split()) == ((streetInfo[2][1][0:-2] + corrected).split()[1:]):  # Control for instances such as Park Place = N Park Pl
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                    elif streetInfo[1][1] != streetInfo[2][1][0:-2]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Cir' in streetInfo[2][1][-3:]:
                    if streetInfo[1][1] == 'Alhambrah Circle' and streetInfo[2][1] == 'Alhambra Cir':
                        continue
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

                elif 'Rd' in streetInfo[2][1][-2:]:
                    if streetInfo[1][1] == 'Saint Johns Road' and streetInfo[2][1] == 'St Johns Rd':
                        continue
                    if streetInfo[1][1] == 'Mount Pleasant Road' and streetInfo[2][1] == 'Mt Pleasant Rd':
                        continue
                    if streetInfo[1][1] == 'Miami Avenue Road' and streetInfo[2][1] == 'SW Miami Ave Rd':
                        continue
                    if streetInfo[1][1] == '63rd Drive' and streetInfo[2][1] == '63rd Rd':
                        continue
                    if streetInfo[1][1] == 'Avenue Street' and streetInfo[2][1] == 'Avenue Rd':
                        continue
                    corrected = streetInfo[2][1][-2:].replace('Rd', 'Road')
                    if len(streetInfo[2][1].split()) > 2:  # Control for instances such as North High Ridge Road = N High Ridge Rd
                        if len(streetInfo[1][1].split()) > 2:
                            if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-2] + corrected).split()[1:]):
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                        else:
                            if (streetInfo[1][1].split()) == ((streetInfo[2][1][0:-2] + corrected).split()[1:]):  # Control for instances such as High Ridge Road = N High Ridge Rd
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                    elif streetInfo[1][1] != streetInfo[2][1][0:-2]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Dr' in streetInfo[2][1][-2:]:
                    if streetInfo[1][1] == 'Wacker Drive' and streetInfo[2][1] == 'N Lower Wacker Dr':
                        continue
                    if streetInfo[1][1] == 'Columbus Drive' and streetInfo[2][1] == 'N Lower Columbus Dr':
                        continue
                    if streetInfo[1][1] == 'Flagler Drive`' and streetInfo[2][1] == 'N Flagler Dr':
                        continue
                    if streetInfo[1][1] == 'Wacker Drive' and (streetInfo[2][1] == 'W Lower Wacker Dr' or streetInfo[2][1] == 'E Lower Wacker Dr' or streetInfo[2][1] == 'S Lower Wacker Dr'):
                        continue
                    corrected = streetInfo[2][1][-2:].replace('Dr', 'Drive')
                    if len(streetInfo[2][1].split()) > 2:  # Control for instances such as North Sunset Drive = N Sunset Dr
                        if len(streetInfo[1][1].split()) > 2:
                            if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-2] + corrected).split()[1:]):
                                continue
                            elif (streetInfo[1][1].split()) == ((streetInfo[2][1][0:-2] + corrected).split()[1:]):
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                        else:
                            if (streetInfo[1][1].split()) == ((streetInfo[2][1][0:-2] + corrected).split()[1:]):  # Control for instances such as Ridge Road = N Ridge Rd
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                    elif streetInfo[1][1] != streetInfo[2][1][0:-2]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Ct' in streetInfo[2][1][-2:]:
                    if streetInfo[1][1] == 'Collins Avenue' and streetInfo[2][1] == 'Collins Ct':
                        continue
                    corrected = streetInfo[2][1][-2:].replace('Ct', 'Court')
                    if len(streetInfo[2][1].split()) > 2:  # Control for instances such as North Delano Court = N Delano Ct
                        if len(streetInfo[1][1].split()) > 2:
                            if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-2] + corrected).split()[1:]):
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                        else:
                            if (streetInfo[1][1].split()) == ((streetInfo[2][1][0:-2] + corrected).split()[1:]):  # Control for instances such as Delano Court = N Delano Ct
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                    elif streetInfo[1][1] != streetInfo[2][1][0:-2]+corrected:
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
                    if streetInfo[1][1] == 'Sandburn Terrace' and streetInfo[2][1] == 'N Sandburg Ter':
                        continue
                    if streetInfo[1][1] == '27th Street Ter' and streetInfo[2][1] == 'NW 27th Ter':
                        continue
                    corrected = streetInfo[2][1][-3:].replace('Ter', 'Terrace')
                    if len(streetInfo[2][1].split()) > 2:  # Control for instances such as Southeast 12th Terrace = SE 12th Ter
                        if len(streetInfo[1][1].split()) > 2:
                            if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-3] + corrected).split()[1:]):
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                        else:
                            if (streetInfo[1][1].split()) == ((streetInfo[2][1][0:-3] + corrected).split()[1:]):  # Control for instances such as 12th Terrace = SE 12th Ter
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                    elif streetInfo[1][1] != streetInfo[2][1][0:-3]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Plz' in streetInfo[2][1][-3:]:
                    corrected = streetInfo[2][1][-3:].replace('Plz', 'Plaza')
                    if len(streetInfo[2][1].split()) > 2:  # Control for instances such as West Lincoln Plaza = W Lincoln Plz
                        if len(streetInfo[1][1].split()) > 2:
                            if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-3] + corrected).split()[1:]):
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                        else:
                            if (streetInfo[1][1].split()) == ((streetInfo[2][1][0:-3] + corrected).split()[1:]):  # Control for instances such as Lincoln Plaza = W Lincoln Plz
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                    elif streetInfo[1][1] != streetInfo[2][1][0:-3]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Hwy' in streetInfo[2][1][-3:]:
                    corrected = streetInfo[2][1][-3:].replace('Hwy', 'Highway')
                    if len(streetInfo[2][1].split()) > 2:  # Control for instances such as North Kings Highway = N Kings Hwy
                        if len(streetInfo[1][1].split()) > 2:
                            if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-3] + corrected).split()[1:]):
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                        else:
                            if (streetInfo[1][1].split()) == ((streetInfo[2][1][0:-3] + corrected).split()[1:]):  # Control for instances such as Kings Highway = N Kings Hwy
                                continue
                            else:
                                row_count += 1
                                output.append(streetInfo)
                                print (streetInfo)
                    elif streetInfo[1][1] != streetInfo[2][1][0:-3]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Blvd' in streetInfo[2][1][-4:]:
                    if streetInfo[1][1] == 'Frederick Douglass BoulevardFrederick Do' and streetInfo[2][1] == 'Frederick Douglass Blvd':
                        continue
                    if streetInfo[1][1] == 'JFK Boulevard' and streetInfo[2][1] == 'John F Kennedy Blvd':
                        continue
                    if streetInfo[1][1] == 'Fulton Market' and streetInfo[2][1] == 'W Fulton Blvd':
                        continue
                    if streetInfo[1][1] == 'North Avenue' and streetInfo[2][1] == 'W North Blvd':
                        continue
                    if streetInfo[1][1] == 'LaSalle Drive' and streetInfo[2][1] == 'N LaSalle Blvd':
                        continue
                    if streetInfo[1][1] == 'Ponce De Leon Boulevard' and streetInfo[2][1] == 'Ponce de Leon Blvd':
                        continue
                    if streetInfo[1][1] == 'Brickell Avenue' and streetInfo[2][1] == 'Brickell Bay Dr':
                        continue
                    if streetInfo[1][1] == 'Brickell Key Drive' and streetInfo[2][1] == 'Brickell Key Blvd':
                        continue
                    corrected = streetInfo[2][1][-4:].replace('Blvd', 'Boulevard')
                    if streetInfo[1][1] != streetInfo[2][1][0:-4]+corrected:
                        if len(streetInfo[2][1].split()) > 2:  # Control for instances such as South Queens Boulevard = S Queens Blvd
                            if len(streetInfo[1][1].split()) > 2:
                                if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-4] + corrected).split()[2:]):
                                    continue
                                else:
                                    row_count += 1
                                    output.append(streetInfo)
                                    print (streetInfo)
                            else:
                                if (streetInfo[1][1].split()) == ((streetInfo[2][1][0:-4] + corrected).split()[1:]):  # Control for instances such as Queens Boulevard = S Queens Blvd
                                    continue
                                else:
                                    row_count += 1
                                    output.append(streetInfo)
                                    print (streetInfo)
                        elif streetInfo[1][1] != streetInfo[2][1][0:-4]+corrected:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)

                elif 'Tpke' in streetInfo[2][1][-4:]:
                    corrected = streetInfo[2][1][-4:].replace('Tpke', 'Turnpike')
                    if streetInfo[1][1] != streetInfo[2][1][0:-4]+corrected:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                elif 'Pkwy' in streetInfo[2][1][-4:]:
                    if streetInfo[1][1] == 'Fullerton Avenue' and streetInfo[2][1] == 'W Fullerton Pkwy':
                        continue
                    if streetInfo[1][1] == 'Dearborn Street' and streetInfo[2][1] == 'N Dearborn Pkwy':
                        continue
                    corrected = streetInfo[2][1][-4:].replace('Pkwy', 'Parkway')
                    if streetInfo[1][1] != streetInfo[2][1][0:-4]+corrected:
                        if len(streetInfo[2][1].split()) > 2:  # Control for instances such as East Diversey Parkway = E Diversey Pkwy
                            if len(streetInfo[1][1].split()) > 2:
                                if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-4] + corrected).split()[2:]):
                                    continue
                                else:
                                    row_count += 1
                                    output.append(streetInfo)
                                    print (streetInfo)
                            else:
                                if (streetInfo[1][1].split()) == ((streetInfo[2][1][0:-4] + corrected).split()[1:]):  # Control for instances such as Diversey Parkway = E Diversey Pkwy
                                    continue
                                else:
                                    row_count += 1
                                    output.append(streetInfo)
                                    print (streetInfo)
                        elif streetInfo[1][1] != streetInfo[2][1][0:-4]+corrected:
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
                    if streetInfo[1][1] == 'Chruch Street' and streetInfo[2][1] == 'Church St':
                        continue
                    if streetInfo[1][1] == 'LaSalle Drive' and streetInfo[2][1] == 'N LaSalle St':
                        continue
                    if streetInfo[1][1] == 'St Andrews Street' and streetInfo[2][1] == 'St Andrew St':
                        continue
                    if streetInfo[1][1] == 'Desplains Street' and (streetInfo[2][1] == 'S Desplaines St' or streetInfo[2][1] == 'N Desplaines St'):
                        continue
                    if streetInfo[1][1] == 'Ontariio Street' and streetInfo[2][1] == 'E Ontario St':
                        continue
                    if streetInfo[1][1] == 'Madison Avenue' and streetInfo[2][1] == 'W Madison St':
                        continue
                    if streetInfo[1][1] == 'NE 2nd Avenue' and streetInfo[2][1] == 'NE 2nd St':
                        continue
                    if streetInfo[1][1] == 'Sixth Street' and streetInfo[2][1] == 'SE 6th St':
                        continue
                    if streetInfo[1][1] == 'Walnuut Street' and streetInfo[2][1] == 'Walnut St':
                        continue
                    if streetInfo[1][1] == 'Halstead Street' and streetInfo[2][1] == 'N Halsted St':
                        continue
                    if streetInfo[1][1] == 'Southwest 74rd Street' and streetInfo[2][1] == 'SW 74th St':
                        continue
                    if streetInfo[1][1] == 'Slate Parkway' and streetInfo[2][1] == 'N State St':
                        continue
                    if streetInfo[1][1] == 'LaSalle Drive' and streetInfo[2][1] == 'N LaSalle St':
                        continue
                    if streetInfo[1][1] == '23th Street' and streetInfo[2][1] == 'NW 23rd St':
                        continue
                    if streetInfo[1][1] == 'Randolph Avenue' and streetInfo[2][1] == 'W Randolph St':
                        continue
                    if streetInfo[1][1] == 'Sixth Street' and streetInfo[2][1] == 'SE 6th St':
                        continue
                    if streetInfo[1][1] == '106th Strett' and streetInfo[2][1] == 'E 106th St':
                        continue
                    if streetInfo[1][1] == 'East Liberty St' and streetInfo[2][1] == 'E Liberty St':
                        continue
                    if streetInfo[1][1] == 'First Street' and streetInfo[2][1] == '1st St':
                        continue
                    if streetInfo[1][1] == 'Chesnut Street' and streetInfo[2][1] == 'Chestnut St':
                        continue
                    if streetInfo[1][1] == 'Cumberland Avenue' and streetInfo[2][1] == 'Cumberland St':
                        continue
                    if streetInfo[1][1] == 'Debvoise Street' and streetInfo[2][1] == 'Debevoise St':
                        continue
                    if streetInfo[1][1] == 'North 4 Street' and streetInfo[2][1] == 'N 4th St':
                        continue
                    if streetInfo[1][1] == 'Shutter Street' and streetInfo[2][1] == 'Shuter St':
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
                    if streetInfo[1][1] == 'Yorkville Street' and streetInfo[2][1] == 'Yorkville Ave':
                        continue
                    if streetInfo[1][1] == 'Michigan Avenue' and (streetInfo[2][1] == 'N Upper Michigan Ave' or streetInfo[2][1] == 'N Lower Michigan Ave'):
                        continue
                    if streetInfo[1][1] == 'Illinois Street' and streetInfo[2][1] == 'E Upper Illinois Ave':
                        continue
                    if streetInfo[1][1] == 'South Sapodilla Ave' and streetInfo[2][1] == 'S Sapodilla Ave':
                        continue
                    if streetInfo[1][1] == 'MIchigan Avenue' and streetInfo[2][1] == 'N Michigan Ave':
                        continue
                    if streetInfo[1][1] == 'Buena Vista Boulevard' and streetInfo[2][1] == 'Buena Vista Ave':
                        continue
                    if streetInfo[1][1] == 'Wilwaukee Avenue' and streetInfo[2][1] == 'N Milwaukee Ave':
                        continue
                    if streetInfo[1][1] == 'Diversey Parkway' and streetInfo[2][1] == 'W Diversey Ave':
                        continue
                    if streetInfo[1][1] == 'Lawerence Avenue' and streetInfo[2][1] == 'W Lawrence Ave':
                        continue
                    if streetInfo[1][1] == 'DeKalb Avenue' and streetInfo[2][1] == 'De Kalb Ave':
                        continue
                    if streetInfo[1][1] == 'Farmham Avenue' and streetInfo[2][1] == 'Farnham Ave':
                        continue
                    if (streetInfo[1][1] == 'Arther Avenue' or streetInfo[1][1] == 'Arthir Avenue' or streetInfo[1][1] == 'Arthur Aveue') and streetInfo[2][1] == 'Arthur Ave':
                        continue
                    if streetInfo[1][1] == 'Batavia Drive' and streetInfo[2][1] == 'Batavia Ave':
                        continue
                    if streetInfo[1][1] == 'Bedfird Avenue' and streetInfo[2][1] == 'Bedford Ave':
                        continue
                    if streetInfo[1][1] == 'Greepoint Avenue' and streetInfo[2][1] == 'Greenpoint Ave':
                        continue
                    if streetInfo[1][1] == 'Manahattan Avenue' and streetInfo[2][1] == 'Manhattan Ave':
                        continue
                    if streetInfo[1][1] == 'Manning Avneue' and streetInfo[2][1] == 'Manning Ave':
                        continue
                    if streetInfo[1][1] == 'River Avenue' and streetInfo[2][1] == 'Rivera Ave':
                        continue
                    if streetInfo[1][1] == "St Mark's Avenue" and streetInfo[2][1] == 'St Marks Ave':
                        continue
                    if streetInfo[1][1] == 'Walker Street' and streetInfo[2][1] == 'Walker Ave':
                        continue
                    if streetInfo[1][1] == 'Weschester Avenue' and streetInfo[2][1] == 'Westchester Ave':
                        continue
                    if streetInfo[1][1] == 'Whittaker Avenue' and streetInfo[2][1] == 'Whitaker Ave':
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

                        elif len(streetInfo[2][1].split()) > 2:  # Control for instances such as West Fullerton Avenue = W Fullerton Ave
                            if len(streetInfo[1][1].split()) > 2:
                                if (streetInfo[1][1].split())[1:] == ((streetInfo[2][1][0:-3] + corrected).split()[1:]):
                                    continue
                                else:
                                    row_count += 1
                                    output.append(streetInfo)
                                    print (streetInfo)
                            else:
                                if (streetInfo[1][1].split()) == ((streetInfo[2][1][0:-3] + corrected).split()[1:]):  # Control for instances such as Fullerton Avenue = W Fullerton Ave
                                    continue
                                else:
                                    row_count += 1
                                    output.append(streetInfo)
                                    print (streetInfo)

                        else:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)

                elif 'Ave N' in streetInfo[2][1][-5:]:  # Avenue N = Avenue
                    corrected = streetInfo[2][1][-5:].replace('Ave N', 'Avenue')
                    if streetInfo[1][1] != streetInfo[2][1][0:-5] + corrected:
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

                elif 'Ave W' in streetInfo[2][1][-5:]:  # Avenue W = Avenue West or Avenue
                    if 'Avenue West' in streetInfo[1][1]:
                        corrected = streetInfo[2][1][-5:].replace('Ave W', 'Avenue West')
                        if streetInfo[1][1] != streetInfo[2][1][0:-5] + corrected:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)
                    elif 'Avenue' in streetInfo[1][1]:
                        corrected = streetInfo[2][1][-5:].replace('Ave W', 'Avenue')
                        if streetInfo[1][1] != streetInfo[2][1][0:-5] + corrected:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)

                elif 'Ave E' in streetInfo[2][1][-5:]:  # Avenue E = Avenue East or Avenue
                    if 'Avenue East' in streetInfo[1][1]:
                        corrected = streetInfo[2][1][-5:].replace('Ave E', 'Avenue East')
                        if streetInfo[1][1] != streetInfo[2][1][0:-5] + corrected:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)
                    elif 'Avenue' in streetInfo[1][1]:
                        corrected = streetInfo[2][1][-5:].replace('Ave E', 'Avenue')
                        if streetInfo[1][1] != streetInfo[2][1][0:-5] + corrected:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)

                elif 'St W' in streetInfo[2][1][-4:]:  # Street W = Street West or Street
                    if streetInfo[1][1] == 'Adalaide Street' and streetInfo[2][1] == 'Adelaide St W':
                        continue
                    if streetInfo[1][1] == 'Queens Street West' and streetInfo[2][1] == 'Queen St W':
                        continue
                    if streetInfo[1][1] == 'Bllor Street' and streetInfo[2][1] == 'Bloor St W':
                        continue
                    if (streetInfo[1][1] == 'Queen Street Weset' or streetInfo[1][1] == 'Queen Street Wset' or streetInfo[1][1] == 'Quene Street West') and streetInfo[2][1] == 'Queen St W':
                        continue
                    if streetInfo[1][1] == 'Richmondd Street West' and streetInfo[2][1] == 'Richmond St W':
                        continue
                    if streetInfo[1][1] == 'Wellesly Street' and streetInfo[2][1] == 'Wellesley St W':
                        continue
                    if 'Street West' in streetInfo[1][1]:
                        corrected = streetInfo[2][1][-4:].replace('St W', 'Street West')
                        if streetInfo[1][1] != streetInfo[2][1][0:-4] + corrected:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)
                    elif 'Street' in streetInfo[1][1]:
                        corrected = streetInfo[2][1][-4:].replace('St W', 'Street')
                        if streetInfo[1][1] != streetInfo[2][1][0:-4] + corrected:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)

                elif 'St E' in streetInfo[2][1][-4:]:  # Street E = Street East or Street
                    if 'Street East' in streetInfo[1][1]:
                        corrected = streetInfo[2][1][-4:].replace('St E', 'Street East')
                        if streetInfo[1][1] != streetInfo[2][1][0:-4] + corrected:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)
                    elif 'Street' in streetInfo[1][1]:
                        corrected = streetInfo[2][1][-4:].replace('St E', 'Street')
                        if streetInfo[1][1] != streetInfo[2][1][0:-4] + corrected:
                            row_count += 1
                            output.append(streetInfo)
                            print (streetInfo)

                elif streetInfo[1][1][0:3] == '1/2':  # Controlling for instances of this unique case (i.e., 1/2 31st St NW = 31st St NW)
                    if streetInfo[1][1][4:] == streetInfo[2][1]:
                        continue
                    else:
                        row_count += 1
                        output.append(streetInfo)
                        print (streetInfo)

                # Control for certain unique instances
                elif streetInfo[1][1] == 'Greenwich Street' and streetInfo[2][1] == 'Greenwich Mews':
                    continue

                elif streetInfo[1][1] == 'Union Square' and streetInfo[2][1] == 'Union Sq E':
                    continue

                elif streetInfo[1][1] == 'Lincoln Road' and streetInfo[2][1] == 'Lincoln Rd Mall':
                    continue

                elif streetInfo[1][1] == 'Queens Quay West' and streetInfo[2][1] == 'Queens Quay W':
                    continue

                elif streetInfo[1][1] == 'Queens Quay East' and streetInfo[2][1] == 'Queens Quay E':
                    continue

                elif streetInfo[1][1] == 'Route 17' and (streetInfo[2][1] == 'RT-17 S' or streetInfo[2][1] == 'RT-17 N'):
                    continue

                elif streetInfo[1][1] == 'North Lincoln Lane' and streetInfo[2][1] == 'Lincoln Ln N':
                    continue

                elif streetInfo[1][1] == 'Canal Towpath NW' and streetInfo[2][1] == 'C&O Canal Towpath NW':
                    continue

                elif streetInfo[1][1] == 'Prospect St. NW' and streetInfo[2][1] == 'Prospect St NW':
                    continue

                elif (streetInfo[1][1] == "Cady's Alley NW" or streetInfo[1][1] == "Cadys Alley NW") and streetInfo[2][1] == 'Cadys Aly NW':
                    continue

                elif streetInfo[1][1] == 'Thomas Jefferson St. NW Ste 600' and streetInfo[2][1] == 'Thomas Jefferson St NW':
                    continue

                elif streetInfo[1][1] == 'Grace Street NW' and streetInfo[2][1] == 'Grace St NW':
                    continue

                elif streetInfo[1][1] == 'Fulton Market' and streetInfo[2][1] == 'W Fulton Market':
                    continue

                elif streetInfo[1][1] == 'Broadway' and streetInfo[2][1] == 'W Broadway':
                    continue

                elif streetInfo[1][1] == 'Queens Plaza' and (streetInfo[2][1] == 'Queens Plz N' or streetInfo[2][1] == 'Queens Plz S'):
                    continue

                elif streetInfo[1][1] == 'Flatbush Avenue Extension' and streetInfo[2][1] == 'Flatbush Ave Ext':
                    continue

                elif streetInfo[1][1] == 'River Avenue' and streetInfo[2][1] == 'Rivera Avenue':
                    continue

                elif streetInfo[1][1] == 'Lincoln Park' and streetInfo[2][1] == 'N Lincoln Park West':
                    continue

                elif streetInfo[1][1] == 'Broadway Street' and streetInfo[2][1] == 'N Broadway':
                    continue

                elif (streetInfo[1][1] == 'M St NW NW' or streetInfo[1][1] == 'M St. NW') and streetInfo[2][1] == 'M St NW':
                    continue

                elif streetInfo[1][1] == 'M St & Penn Ave & 28th St' and streetInfo[2][1] == 'M St NW':
                    continue

                elif streetInfo[1][1] == 'P St & 26th St' and streetInfo[2][1] == '26th St NW':
                    continue

                elif streetInfo[1][1] == '34th St. and Volta Place NW' and streetInfo[2][1] == '34th St NW':
                    continue

                elif streetInfo[1][1] == 'Wisconsin Avenue NW' and streetInfo[2][1] == 'Wisconsin Ave NW':
                    continue

                elif streetInfo[1][1] == 'P St. NW' and streetInfo[2][1] == 'P St NW':
                    continue

                elif streetInfo[1][1] == 'Riverside Plaza' and streetInfo[2][1] == 'Riverside':
                    continue

                elif streetInfo[1][1] == 'Biscayne Boulevard' and streetInfo[2][1] == 'Biscayne Boulevard Way':
                    continue

                elif streetInfo[1][1] == 'Post Road East' and streetInfo[2][1] == 'Post Rd W':
                    continue

                elif streetInfo[1][1] == 'Delano Court' and streetInfo[2][1] == 'S Delano Ct E':
                    continue

                elif streetInfo[1][1] == 'Route 22' and streetInfo[2][1] == 'US-22':
                    continue

                elif streetInfo[1][1] == 'Palmer Square' and (streetInfo[2][1] == 'Palmer Sq W' or streetInfo[2][1] == 'Palmer Sq E' or streetInfo[2][1] == 'Palmer Sq S'):
                    continue

                elif streetInfo[1][1] == 'Broadway R' and streetInfo[2][1] == 'Broadway':
                    continue

                elif streetInfo[1][1] == '34th St NW NW' and streetInfo[2][1] == '34th St NW':
                    continue

                elif streetInfo[1][1] == '34th Street' and streetInfo[2][1] == '34th St NW':
                    continue

                elif streetInfo[1][1] == 'Grace St. NW' and streetInfo[2][1] == 'Grace St NW':
                    continue

                elif streetInfo[1][1] == 'Queens Quay West' and streetInfo[2][1] == 'Queens Quay E':
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
        with open('RetailCountryObjectID.csv', 'wb') as output_file:
            objectID_data_writer = csv.DictWriter(output_file, fieldnames=['OBJECTID', 'label', 'StreetNa_1', 'county', 'labelDirec', 'Angle'],
                                                  extrasaction='ignore', delimiter=',', quotechar='"')

            objectID_data_writer.writeheader()

            for entry in output:
                objectID_data_writer.writerow({'OBJECTID': entry[0][1], 'label': entry[1][1], 'StreetNa_1': entry[2][1], 'county': entry[3][1], 'labelDirec': entry[4][1], 'Angle': entry[5][1]})
                # Write row to CSV file consisting of OBJECTID, label, StreetNa_1, county, labelDirec, and Angle for incorrect data

    print ("")
    print ("-----------------------------")
    print ("")
    print (str(row_count) + " labels did not match")
    print ("")


if __name__ == '__main__':
    main()