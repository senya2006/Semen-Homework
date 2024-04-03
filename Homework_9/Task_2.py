import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('csv_email_file.csv', 'w', newline='') as csv_email_file:
        csv_writer = csv.writer(csv_email_file)

        for line in csv_reader:
            email = line[2]
            csv_writer.writerow([email])
