import csv


def main():

    with open('Angles_1.csv', 'r') as input_file:
        angle_data_reader = csv.DictReader(input_file, delimiter='\t', quotechar='"')

        data_dict = {}

        for line in angle_data_reader:
            values = line.values()[0]
            street_name2 = values.split(',')[0]
            angles = values.split(',')[1]
            data_dict[street_name2] = angles

    with open('RetailManhattanObjectID.csv') as input_file2:
        reader = csv.reader(input_file2, delimiter=",")

        for row in reader:
            objectID = row[0]
            street_name = row[1]
            labelside = row[3]

            if street_name == 'SixthAvenue':
                street_name = street_name.replace('SixthAvenue', 'Sixth Avenue')
            elif street_name == 'FIfth Avenue':
                street_name = street_name.replace('FIfth Avenue', 'Fifth Avenue')

            if street_name in data_dict.keys():
                pair = (street_name, data_dict[street_name])

                with open('AngleLabels.csv', 'ab') as output_file:
                    angle_data_writer = csv.writer(output_file, delimiter=',')
                    angle_data_writer.writerow([pair[0], pair[1], objectID, labelside])
                    print (pair[0], pair[1], objectID, labelside)
                    output_file.flush()


if __name__ == '__main__':
    main()