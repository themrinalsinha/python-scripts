import csv

with open('new_data.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file)
    csv_new = []
    with open('text.csv' , 'r') as old_file:
        csv_reader = csv.reader(old_file)
        for i, line in enumerate(csv_reader):
            csv_new.append(line)
            print(line)
            if line[1] == '':
                csv_new[-2][-6] += ' ' + line[2]
                csv_new.pop()
        for rows in csv_new:
            print(rows)
            csv_writer.writerow(rows)